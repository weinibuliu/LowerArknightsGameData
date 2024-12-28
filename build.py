# please run: python build.py {Language} {Github Token}

import os
import json
import sys
import shutil
import subprocess
from pathlib import Path
from datetime import datetime

from src import avatar, character
from src.commit import get_versions

LANGS = ["zh_CN", "en_US", "ja_JP", "ko_KR"]

# 检查当前版本信息
curent_version_path = Path(Path.cwd(), "version.json")
vers = {}
if curent_version_path.exists():
    with open(curent_version_path, "r", encoding="utf-8") as f:
        vers: dict = json.load(f)
currentt_vers = {
    "zh_CN ": vers.get("zh_CN"),
    "en_US": vers.get("en_US"),
    "ja_JP": vers.get("ja_JP"),
    "ko_KR": vers.get("ko_KR"),
}
print(f"Current Version: {currentt_vers}")

# 检查目标版本信息
release = "false"
target_versions = get_versions()
cn_ver_path = Path(Path.cwd(), "zh_CN/version")
if cn_ver_path.exists():
    with open(cn_ver_path, "r", encoding="utf-8") as cnv:
        cn_ver = cnv.read()
        target_versions.update({"zh_CN": cn_ver})

for lang in ["en_US", "ja_JP", "ko_KR"]:
    current_ver = currentt_vers.get(lang)
    target_ver = target_versions.get(lang)
    if current_ver is None and target_ver is not None:
        release = "true"
        break
    elif (
        current_ver is not None and target_ver is not None and current_ver < target_ver
    ):
        release = "true"
        break

if release != "true":
    print("Exit caused by release == 'false'.")
    subprocess.run("echo '::notice :: Exit caused by release == 'false'", shell=True)
    exit()

subprocess.run("echo '::notice :: 'Test''", shell=True)  #
print(f"Target Version: {target_versions}")


with open(f"version.json", "w", encoding="utf-8") as v:
    json.dump(target_versions, v, indent=4, ensure_ascii=False)

# 执行构建
for lang in LANGS:
    character.run(lang)
avatar.run()

# 写入 GITHUB ENV
if os.environ.get("CI"):
    subprocess.run(f'echo "release={release}" >> "$GITHUB_ENV"', shell=True)
    print(f"env.release = {release}")

print("Done: Version")
print("\nAll Done!")
print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")

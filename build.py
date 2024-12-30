# please run: python build.py {Language} {Github Token}

import os
import json
import sys
import shutil
import subprocess
from pathlib import Path
from datetime import datetime

from src import avatar, character
from src.version import get_commit

# 检查当前版本信息
curent_version_path = Path(Path.cwd(), "version.json")
vers = {}
with open(curent_version_path, "r", encoding="utf-8") as f:
    version: dict = json.load(f)
    current_sha = version.get("Sha")


# 检查目标版本信息
commit_info = get_commit()
target_sha = commit_info["sha"]
update_time = commit_info["update_time"]
if current_sha == target_sha:
    print("Exit caused by release == 'false'.")
    subprocess.run("echo '::notice :: Exit caused by release == 'false'", shell=True)
    exit()
print(f"Target Sha: {target_sha}")

version.pop("gacha")
version["Sha"] = target_sha

with open(f"version.json", "w", encoding="utf-8") as v:
    json.dump(version, v, indent=4, ensure_ascii=False)


# 写入 GITHUB ENV
if os.environ.get("CI"):
    subprocess.run(f'echo "update_time={update_time}" >> "$GITHUB_ENV"', shell=True)
    subprocess.run(f'echo "release=true" >> "$GITHUB_ENV"', shell=True)
    print(f"env.update_time = {update_time}")
    print(f"env.release = 'true'")

print("Done: Version")
print("\nAll Done!")
print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")

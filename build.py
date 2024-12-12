# please run: python build.py {Language} {Timestamp} {Github Token}

import os
import sys
import shutil
import subprocess
from pathlib import Path
from datetime import datetime

from src import avatar, character, char_classisy
from src import cwd, build_path, cache_path
from src.commit import get_version

lang = sys.argv[1]
print(f"Language: {lang}")

character.run(lang)
char_classisy.run(lang)
avatar.run(lang)
print()

# 写入版本信息
ver = version = existing_version = current_version = None
existing_version_path = Path(cwd, f"version/{lang}/version")

if lang == "zh_CN":
    with open(f"{cache_path}/zh_CN/version", "r", encoding="utf-8") as cv:
        current_version = cv.readline().replace("\n", "")
else:
    current_version = get_version(lang)
print(f"Current Version: {current_version}")

with open(f"{build_path}/version", "w", encoding="utf-8") as vs:
    if existing_version_path.exists():
        with open(existing_version_path, "r", encoding="utf-8") as ev:
            existing_version = ev.readline().replace("\n", "")
    print(f"Existing Version: {existing_version}")

    if current_version is not None:
        ver = current_version.split("-")
        version = f"{ver[0]}{ver[1]}{ver[2]}{ver[3]}{ver[4]}{ver[5]}"

    built_timestamp = int(sys.argv[2])
    built_time = datetime.fromtimestamp(built_timestamp)

    vs.write(f"{current_version}\n")
    vs.write(f"{version}\n")
    vs.write(f"built_time: {built_time}\n")
    vs.write(f"built_timestamp: {built_timestamp}")

with open(f"{build_path}/{lang}-version", "w", encoding="utf-8") as vl:
    vl.write(current_version)

shutil.copyfile(Path(build_path, "version"), existing_version_path)

release = "false"
change = None
# 写入 GITHUB ENV
if os.environ.get("CI"):
    subprocess.run(f'echo ver={current_version} >> "$GITHUB_ENV"', shell=True)
    if current_version is not None and current_version != existing_version:
        release = "true"
        change = f"{existing_version} -> {current_version}"

    subprocess.run(f'echo release={release} >> "$GITHUB_ENV"', shell=True)
    subprocess.run(f'echo change={change} >> "$GITHUB_ENV"', shell=True)
    print(f"env.release = {release}")
    print(f"env.change = {change}")
    print(f"env.ver = {current_version}")

print("Done: Version")
print("\nAll Done!")
print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")

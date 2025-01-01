# please run: python build.py {Language} {Github Token}

import os
import json
import subprocess
from pathlib import Path

from src import avatar, character
from src.version import get_commit


# 检查当前版本信息
with open("version.json", "r", encoding="utf-8") as f:
    current_sha: dict = json.load(f).get("Sha")


# 检查目标版本信息
commit_info = get_commit()
target_sha = commit_info["sha"]
update_time = commit_info["update_time"]
update_ts = commit_info["update_ts"]
if current_sha == target_sha:
    print("Exit caused by release == 'false'.")
    subprocess.run("echo '::notice :: Exit caused by release == 'false'", shell=True)
    exit()
print(f"Target Sha: {target_sha}")


# 获取各区服版本信息
with open("cache/resource/version.json", "r", encoding="utf-8") as f:
    cnver: dict = json.load(f)
    cnver.pop("gacha", None)

with open(
    "cache/resource/global/txwy/resource/version.json", "r", encoding="utf-8"
) as f:
    twver: dict = json.load(f)
    twver.pop("gacha", None)

with open(
    "cache/resource/global/YoStarEN/resource/version.json", "r", encoding="utf-8"
) as f:
    enver: dict = json.load(f)
    enver.pop("gacha", None)

with open(
    "cache/resource/global/YoStarJP/resource/version.json", "r", encoding="utf-8"
) as f:
    jpver: dict = json.load(f)
    jpver.pop("gacha", None)

with open(
    "cache/resource/global/YoStarKR/resource/version.json", "r", encoding="utf-8"
) as f:
    krver: dict = json.load(f)
    krver.pop("gacha", None)

vers = {
    "Sha": target_sha,
    "CN": cnver,
    "TW": twver,
    "EN": enver,
    "JP": jpver,
    "KR": krver,
}

with open(f"version.json", "w", encoding="utf-8") as v:
    json.dump(vers, v, indent=4, ensure_ascii=False)

character.run()
avatar.run()

# 写入 GITHUB ENV
if os.environ.get("CI"):
    subprocess.run(f'echo "update_time={update_time}" >> "$GITHUB_ENV"', shell=True)
    subprocess.run(f'echo "update_ts={update_ts}" >> "$GITHUB_ENV"', shell=True)
    subprocess.run(f'echo "release=true" >> "$GITHUB_ENV"', shell=True)
    print(f"env.update_time = {update_time}")
    print(f"env.update_ts = {update_ts}")
    print(f"env.release = 'true'")

print("Done: Version")
print("\nAll Done!")
print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")

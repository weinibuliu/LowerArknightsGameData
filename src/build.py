# python build.py {Language} {Github Token}

import json
import subprocess
from pathlib import Path

from . import avatar, character
from . import version


def run():
    # 检查当前版本信息
    VERSION_PATH = Path(Path.cwd(), "res/version")
    current_sha = current_ts = None
    if VERSION_PATH.exists():
        with open(VERSION_PATH, "r", encoding="utf-8") as f:
            current_sha: str = f.readline().replace("\n", "")
            current_ts: int = int(f.readline().replace("\n", ""))
    print(f"Current Sha: {current_sha}")
    print(f"Current Timestamp: {current_ts}")

    # 检查目标版本信息
    target_sha = version.get_commit_sha()
    target_ts = version.get_timestamp()
    print(f"Target Sha: {target_sha}")
    print(f"Target Timestamp: {target_ts}")
    if current_sha == target_sha or current_ts == target_ts:
        print("Exit caused by release == 'false'.")
        exit()  # 退出脚本

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
        "Commit Sha": target_sha,
        "CN": cnver,
        "TW": twver,
        "EN": enver,
        "JP": jpver,
        "KR": krver,
    }

    VERSION_JSON_PATH = Path(Path.cwd(), "version.json")
    with open(VERSION_JSON_PATH, "w", encoding="utf-8") as v:
        json.dump(vers, v, indent=4, ensure_ascii=False)
        print(vers)
    with open(VERSION_PATH, "w", encoding="utf-8") as v:
        v.write(f"{target_sha}\n")
        v.write(f"{target_ts}")

    character.run()
    avatar.run()

    # 写入 GITHUB ENV
    subprocess.run(f'echo "release=true" >> "$GITHUB_ENV"', shell=True)
    print(f"env.release = 'true'")

    print("Done: Version")
    print("\nAll Done!")

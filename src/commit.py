# 获取 https://www.github.com/Kengxxiao/ArknightsGameData_YoStar 的 commit message
# 适用范围： en_US | ja_JP | ko_KR

import sys
from typing import Literal
from datetime import datetime, timedelta

from github import Github

token = None
if len(sys.argv) > 3:
    token = sys.argv[3]

until = datetime.now()
since = until - timedelta(30)

gh = Github(login_or_token=token, per_page=15, seconds_between_requests=2)
repo = gh.get_repo("Kengxxiao/ArknightsGameData_YoStar")


def get_commit_msg(lang: Literal["en_US", "ja_JP", "ko_KR"]) -> str:
    if lang not in ["en_US", "ja_JP", "ko_KR"]:
        raise ValueError(f"{lang} is not supported langugae.")

    repo = gh.get_repo("Kengxxiao/ArknightsGameData_YoStar")

    if lang == "en_US":
        flag = lang.split("_")[0].upper()
    else:
        flag = lang.split("_")[1]

    commits = repo.get_commits(
        path=f"{lang}/gamedata",
        since=since,
        until=until,
    ).get_page(0)

    for commit in commits:
        msg = commit.commit.message
        if flag in msg:
            return msg


def get_version(lang: str) -> str | None:
    msg = get_commit_msg(lang)
    if msg is None:
        raise RuntimeError("Version is None.Please check the repo.")
    ver = msg.split("Data:")[-1]
    return ver


if __name__ == "__main__":
    for lang in ["en_US", "ja_JP", "ko_KR"]:
        ver = get_version(lang)
        print(f"{lang}: {ver}")

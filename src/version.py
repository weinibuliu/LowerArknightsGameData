# 获取 https://www.github.com/Kengxxiao/ArknightsGameData_YoStar 的 commit message
# 适用范围： en_US | ja_JP | ko_KR

import sys
import time
from typing import Literal, List
from datetime import datetime, timedelta

from github import Github

# from src import timestamp

token = None
if len(sys.argv) >= 2:
    token = sys.argv[1]

UNTIL = datetime.now()
SINCE = UNTIL - timedelta(30)

GH = Github(login_or_token=token, per_page=30, seconds_between_requests=2, retry=None)
REPO = GH.get_repo("MaaAssistantArknights/MaaAssistantArknights")


def get_commit() -> str:
    commits = REPO.get_commits(
        path="resource/version.json",
        since=SINCE,
        until=UNTIL,
    ).get_page(0)
    commit = commits[0]
    return {
        "sha": commit.commit.sha,
        "update_time": str(commit.commit.last_modified_datetime)
        .split("+")[0]
        .replace(" ", ""),
    }


if __name__ == "__main__":
    print(get_commit())

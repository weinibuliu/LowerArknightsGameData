# 检查目标版本

import json
import sys
from pathlib import Path
from datetime import datetime, timedelta

from github import Github

token = None
if len(sys.argv) >= 2:
    token = sys.argv[1]

UNTIL = datetime.now()
SINCE = UNTIL - timedelta(30)
GH = Github(login_or_token=token, per_page=30, seconds_between_requests=2, retry=None)
REPO = GH.get_repo("MaaAssistantArknights/MaaAssistantArknights")

VERSION_JSON_PATH = Path(Path.cwd(), "cache/resource/version.json")


def get_commit_sha() -> str:
    sha = None
    commits = REPO.get_commits(
        path="resource/version.json",
        since=SINCE,
        until=UNTIL,
    ).get_page(0)
    sha = commits[0].commit.sha
    return sha


def get_timestamp() -> int:
    ts = 0
    if VERSION_JSON_PATH.exists():
        with open(VERSION_JSON_PATH, "r", encoding="utf-8") as f:
            data: dict = json.load(f)
            update_time: str = data["last_updated"]
            ts = int(datetime.strptime(update_time, "%Y-%m-%d %H:%M:%S.%f").timestamp())
    return ts

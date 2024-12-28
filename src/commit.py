# 获取 https://www.github.com/Kengxxiao/ArknightsGameData_YoStar 的 commit message
# 适用范围： en_US | ja_JP | ko_KR

import sys
import time
from typing import Literal, List
from datetime import datetime, timedelta

from github import Github
from github.Commit import Commit

token = None
if len(sys.argv) >= 2:
    token = sys.argv[1]

until = datetime.now()
since = until - timedelta(30)

langs = ["en_US", "ja_JP", "ko_KR"]
gh = Github(login_or_token=token, per_page=15, seconds_between_requests=2)
repo = gh.get_repo("Kengxxiao/ArknightsGameData_YoStar")


def _get_commits() -> List[Commit]:
    commits = repo.get_commits(
        since=since,
        until=until,
    ).get_page(0)

    if commits is None:
        raise RuntimeError("Commits is None.Please check the repo.")
    else:
        return commits


def _get_version(
    commits: List[Commit],
    lang: Literal["en_US", "ja_JP", "ko_KR"],
) -> dict[str]:
    if lang == "en_US":
        flag = "EN"
    else:
        flag = lang.split("_")[-1]

    version = {lang: None}
    for c in commits:
        if flag in c.commit.message:
            ver = c.commit.message.split("Data:")[-1]
            version[lang] = ver
            break
    return version


def get_versions() -> dict[str]:
    commits = _get_commits()
    versions = {"build_timestamp": int(time.time())}
    for lang in langs:
        ver = _get_version(commits, lang)
        versions.update(ver)
    return versions


if __name__ == "__main__":
    print(get_versions())

import sys
from typing import List

from github import Github, Issue

whetherclose = sys.argv[1]  #'true'(close)|| 'false'(open)
lang = sys.argv[2]
token = sys.argv[3]
action_id = sys.argv[4]
action_num = sys.argv[5]

repo = Github(login_or_token=token).get_repo("weinibuliu/LowerArknightsGameData")


def open():
    repo.create_issue(
        title=f"{lang} didn't build",
        body=f"{lang} didn't build,please check Github Action.\nhttps://github.com/weinibuliu/LowerArknightsGameData/actions/runs/{action_id}  ({action_num})\n@weinibuliu",
        labels=f"bug: {lang}",
    )


def close():
    all_issues = repo.get_issues(state="open", labels=[f"bug: {lang}"])

    issues: List[Issue.Issue] = []
    new_issue = []
    num = 0
    while new_issue == [] and num <= 5:
        new_issue = []
        new_issue = all_issues.get_page(num)
        issues.append(i for i in new_issue)
        num += 1

    for issue in issues:
        print(type(issue), issue)
        print(issue.body)
        issue.create_comment(
            f"According to the operation of https://github.com/weinibuliu/LowerArknightsGameData/actions/runs/{action_id}  ({action_num}), the data building of {lang} has returned to normal.\nTherefore, this issue will be marked as completed and closed."
        )
        issue.edit(state="close", state_reason="completed")
        print(f"Close {issue.number}")


if whetherclose == "true":
    close()
elif whetherclose == "false":
    open()
else:
    raise ValueError(f"{whetherclose} is not a correct value. ('true' | 'false')")

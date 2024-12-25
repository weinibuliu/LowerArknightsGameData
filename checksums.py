import hashlib
import subprocess
import sys
from pathlib import Path


from github import Github

token = sys.argv[1]

gh = Github(login_or_token=token, retry=None)
repo = gh.get_repo("weinibuliu/LowerArknightsGameData")
release = repo.get_latest_release()
assets = release.assets
print(release.body)

md5s = {}
for a in assets:
    if ".zip" not in a.name:
        continue
    path = Path(Path.cwd(), "assets", a.name)
    with open(path, "rb") as file:
        data = file.read()

    md5 = hashlib.md5(data).hexdigest()
    print(f"{a.name.split(".")[0]}_MD5: {md5}")

    md5s[a.name.split(".")[0]] = md5
    a.update_asset(a.name, md5)

release.update_release(
    message=release.body
    + f"### MD5\n\n- zh_CN: {md5s["zh_CN"]}\n- en_US: {md5s["en_US"]}\n-ja_JP: {md5s["ja_JP"]}\n -ko_KR: {md5s["ko_KR"]}"
)

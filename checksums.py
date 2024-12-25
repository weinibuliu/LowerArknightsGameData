import hashlib
import sys
from pathlib import Path


from github import Github

token = sys.argv[1]

gh = Github(login_or_token=token, retry=None)
repo = gh.get_repo("weinibuliu/LowerArknightsGameData")
release = repo.get_latest_release()
assets = release.assets
for a in assets:
    with open(Path(Path.cwd(), a.name), "rb") as file:
        data = file.read()
        md5 = hashlib.md5().hexdigest()
    a.update_asset(a.name, md5)

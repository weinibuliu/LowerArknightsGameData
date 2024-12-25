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
    if ".zip" not in a.name:
        continue

    path = Path(Path.cwd(), "assets", a.name)
    with open(path, "rb") as file:
        data = file.read()

    md5 = hashlib.md5(data).hexdigest()
    sha256 = hashlib.sha256(data).hexdigest()
    print(f"{a.name} Path: {path}")
    print(f"{a.name}: {md5}")

    a.update_asset(a.name, md5)

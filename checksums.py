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

for a in assets:
    if ".zip" not in a.name:
        continue

    path = Path(Path.cwd(), "assets", a.name)
    with open(path, "rb") as file:
        data = file.read()

    md5 = hashlib.md5(data).hexdigest()
    print(f"{a.name} Path: {path}")
    print(f"{a.name}: {md5}")

    subprocess.check_call(
        f'echo {a.name.split(".")[0]}_MD5={md5} >> "$GITHUB_ENV"', shell=True
    )
    a.update_asset(a.name, md5)

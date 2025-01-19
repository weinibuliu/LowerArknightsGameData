import hashlib
import subprocess
from pathlib import Path


def run():
    release_path = Path(Path.cwd(), "build/GameResource.zip")
    with open(release_path, "rb") as file:
        data = file.read()
    sha = hashlib.sha256(data).hexdigest()
    with open("GameResource.zip.sha256", "w", encoding="utf-8") as f:
        f.write(sha)
    subprocess.run(f'echo sha={sha} >> "$GITHUB_ENV"', shell=True)
    print(f"env.sha = {sha}")

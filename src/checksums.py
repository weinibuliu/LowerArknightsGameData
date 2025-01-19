import hashlib
import subprocess
from pathlib import Path


def run():
    release_path = Path(Path.cwd(), "build/GameResource.zip")
    with open(release_path, "rb") as file:
        data = file.read()
    sha256 = hashlib.sha256(data).hexdigest()
    with open("GameResource.zip.sha256", "w", encoding="utf-8") as f:
        f.write(sha256)
    subprocess.run(f'echo sha256={sha256} >> "$GITHUB_ENV"', shell=True)
    print(f"env.sha256 = {sha256}")

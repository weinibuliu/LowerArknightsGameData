import hashlib
import subprocess
from pathlib import Path


def get_sha():
    release_path = Path(Path.cwd(), "build/GameData.zip")
    with open(release_path, "rb") as file:
        data = file.read()
    sha = hashlib.sha256(data).hexdigest()
    with open("GameData.zip.sha256", "w", encoding="utf-8") as f:
        f.write(sha)
    subprocess.run(f'echo Sha={sha} >> "$GITHUB_ENV"', shell=True)
    print(f"env.Sha = {sha}")


if __name__ == "__main__":
    get_sha()

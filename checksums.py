import hashlib
import subprocess
from pathlib import Path


def make_md5():
    release_path = Path(Path.cwd(), "build/GameData.zip")
    with open(release_path, "rb") as file:
        data = file.read()
    md5 = hashlib.md5(data).hexdigest()
    subprocess.check_call(f'echo MD5={md5} >> "$GITHUB_ENV"', shell=True)
    print(f"MD5 = {md5}")


if __name__ == "__main__":
    make_md5()

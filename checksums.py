import hashlib
import subprocess
from pathlib import Path


md5s = {}
for name in ["zh_CN", "en_US", "ja_JP", "ko_KR"]:
    path = Path(Path.cwd(), "assets", f"{name}.zip")
    with open(path, "rb") as file:
        data = file.read()
    md5 = hashlib.md5(data).hexdigest()
    subprocess.check_call(f'echo {name}_MD5={md5} >> "$GITHUB_ENV"', shell=True)

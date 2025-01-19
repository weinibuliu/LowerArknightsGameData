import time
from pathlib import Path

build_path = Path(Path.cwd(), "build")
avatar_path = Path(build_path, "avatar")
res_path = Path(Path.cwd(), "res")

for path in [build_path, avatar_path, res_path]:
    if not path.exists():
        path.mkdir()

import time
from pathlib import Path

timestamp = int(time.time())

build_path = Path(Path.cwd(), "build")
avatar_path = Path(build_path, "avatar")

for path in [build_path, avatar_path]:
    if not path.exists():
        path.mkdir()

print("\n━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")

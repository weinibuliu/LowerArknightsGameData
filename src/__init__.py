from pathlib import Path

cwd = Path.cwd()
cache_path = Path(Path.cwd(), "cache")
build_path = Path(Path.cwd(), "build")
b_ava_path = Path(build_path, "avatar")
classisy_path = Path(build_path, "char_classisy")

for path in [cache_path, build_path, b_ava_path, classisy_path]:
    if not path.exists():
        path.mkdir()

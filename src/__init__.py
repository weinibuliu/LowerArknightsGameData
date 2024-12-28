from pathlib import Path

build_path = Path(Path.cwd(), "build")

if not build_path.exists():
    build_path.mkdir()

print("\n━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")

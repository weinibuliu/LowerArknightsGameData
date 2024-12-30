# 角色信息
import json
from pathlib import Path


def run():
    build_path = Path(Path.cwd(), "build")
    cache_path = Path(Path.cwd(), "cache")

    with open(Path(build_path, "character.json"), "w", encoding="utf-8") as f:
        json.dump({}, f)

    with open(f"{cache_path}/resource/battle_data.json", "r", encoding="utf-8") as js:
        raw: dict[dict] = json.load(js)["chars"]

    num = 0
    chars = {}
    for key in raw:
        id: str = key  # id
        if "char_" not in id:
            continue

        chars[id] = raw[id]
        chars[id].pop("rangeId", None)
        num += 1

    if num == 0:
        raise RuntimeError("Fail to get characters.")

    with open(f"{build_path}/character.json", "w", encoding="utf-8") as ct:
        json.dump(chars, ct, indent=4, ensure_ascii=False)

    print(f"Done: Character ({num})")


if __name__ == "__main__":
    run()

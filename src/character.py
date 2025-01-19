# 角色信息
import json
from pathlib import Path

from .spchars import SP_CHARS

GLOBALS = ["en", "jp", "kr", "tw"]


def run():
    build_path = Path(Path.cwd(), "build")
    cache_path = Path(Path.cwd(), "cache")

    with open(f"{cache_path}/resource/battle_data.json", "r", encoding="utf-8") as js:
        raw: dict[dict] = json.load(js)["chars"]

    num = 0
    chars = {}
    for key in raw:
        id: str = key  # id
        if "char_" not in id or id in SP_CHARS:
            continue

        chars[id] = raw[id]
        chars[id].pop("rangeId", None)
        for g in GLOBALS:
            unable = chars[id].get(f"name_{g}_unavailable")
            chars[id].pop(f"name_{g}_unavailable", None)
            if unable:
                chars[id][f"name_{g}"] = None
        num += 1

    if num == 0:
        raise RuntimeError("Fail to get characters.")

    with open(f"{build_path}/operators.json", "w", encoding="utf-8") as ct:
        json.dump(chars, ct, indent=4, ensure_ascii=False)

    print(f"Done: Character ({num})")


if __name__ == "__main__":
    run()

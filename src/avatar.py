# 角色头像
import json
import shutil
from pathlib import Path


def run(lang: str):
    build_path = Path(Path.cwd(), "build")
    cache_path = Path(Path.cwd(), "cache", lang)

    with open(Path(build_path, "character_table.json"), "r", encoding="utf-8") as c:
        chars: dict = json.load(c)

    c_ava_path = Path(cache_path, "avatar")
    b_ava_path = Path(build_path, "avatar")

    avatar_paths = [path for path in c_ava_path.rglob("*")]

    num = 0
    chars_list = []
    for char in chars:
        char_1 = f"{char}.png"
        char_2 = f"{char}_2.png"
        chars_list.append(char_1)
        chars_list.append(char_2)

    for a_path in avatar_paths:
        if a_path.name in chars_list:
            shutil.copyfile(a_path, Path(b_ava_path, a_path.name))
            num += 1

    if num == 0:
        raise RuntimeError("Fail to get avatar.")
    else:
        print(f"Done: Avatar ({num})")


if __name__ == "__main":
    run()

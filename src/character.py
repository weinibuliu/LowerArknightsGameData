# 角色信息
import json
from pathlib import Path


def run(lang: str):
    build_path = Path(Path.cwd(), "build")
    if lang == "zh_CN":
        cache_path = Path(Path.cwd(), lang)
    else:
        cache_path = Path(Path.cwd(), "global", lang)

    if not Path(build_path, "character.json").exists():
        with open(Path(build_path, "character.json"), "w", encoding="utf-8") as f:
            json.dump({}, f)

    with open(
        f"{cache_path}/gamedata/excel/character_table.json", "r", encoding="utf-8"
    ) as js:
        raw: dict = json.load(js)
        raw_items: list[list] = list(raw.items())

    num = 0
    characters: dict = {}
    for data in raw_items:
        info: dict = data[-1]
        id: str = data[0]  # id
        if "char_" not in id:
            continue
        num += 1
    if num == 0:
        raise RuntimeError("Fail to get characters.")

    if lang == "zh_CN":
        name: str = info.get("name")  # 名称
        rarity: int = info.get("rarity")  # 稀有度 (0 对应 1星干员)
        profession: str = info.get("profession")  # 职业
        subProfessionId: str = info.get("subProfessionId")  # 子职业
        position: str = info.get("position")  # 部署位置

        characters[id] = {
            "name": name,
            "rarity": rarity,
            "profession": profession,
            "subProfessionId": subProfessionId,
            "position": position,
        }
    else:
        name: str = info.get("name")
        characters[id][f"{lang}_name"] = name

    with open(f"{build_path}/character.json", "r", encoding="utf-8") as f:
        raw: dict = json.load(ct)
    with open(f"{build_path}/character.json", "w", encoding="utf-8") as ct:
        characters = raw.update(characters)
        json.dump(characters, ct, indent=4, ensure_ascii=False)

    print(f"Done: {lang} Character ({num})")


if __name__ == "__main__":
    run()

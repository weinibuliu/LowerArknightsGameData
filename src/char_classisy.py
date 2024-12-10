import json
from pathlib import Path

# from . import build_path

build_path = Path(Path.cwd(), "build")
classisy_path = Path(build_path, "char_classisy")


def _character() -> dict[str, dict]:
    with open(Path(build_path, "character_table.json"), "r", encoding="utf-8") as c:
        chars: dict = json.load(c)
    return chars


def _rarity(lang: str) -> dict[str, dict]:
    if lang == "zh_CN":
        rarity_dict = {"0": {}, "1": {}, "2": {}, "3": {}, "4": {}, "5": {}}
    else:
        rarity_dict = {
            "TIER_1": {},
            "TIER_2": {},
            "TIER_3": {},
            "TIER_4": {},
            "TIER_5": {},
            "TIER_6": {},
        }
    return rarity_dict


def _profession(_chars: dict) -> dict:
    profession_dict = {
        "PIONEER": {},
        "WARRIOR": {},
        "TANK": {},
        "SNIPER": {},
        "CASTER": {},
        "MEDIC": {},
        "SUPPORT": {},
        "SPECIAL": {},
    }
    for char in _chars.items():
        profession = char[1]["profession"]
        subProfession = char[1]["subProfessionId"]
        if subProfession not in profession_dict[profession]:
            profession_dict[profession].update({subProfession: {}})

    return profession_dict


def profession(_chars: dict[str, dict]):
    num = 0
    profession_dict = _profession(_chars)
    for char in _chars.items():
        num += 1
        char_infos = char[-1]
        id = char[0]
        name = char_infos["name"]
        profession = char_infos["profession"]
        subProfession = char_infos["subProfessionId"]
        profession_dict[profession][subProfession].update({name: id})

    with open(Path(classisy_path, "profession.json"), "w", encoding="utf-8") as p:
        json.dump(profession_dict, p, indent=4, ensure_ascii=False)

    if num == 0:
        raise RuntimeError("Fail to classisy characters by profession.")
    else:
        print(f"Done: Profession classification ({num})")


def rarity(_chars: dict[str, dict], lang: str):
    num = 0
    rarity_dict = _rarity(lang)
    for char in _chars.items():
        num += 1
        char_info = char[-1]
        id = char[0]
        name = char_info["name"]
        rarity = str(char_info["rarity"])
        rarity_dict[rarity].update({id: name})

    with open(Path(classisy_path, "rarity.json"), "w", encoding="utf-8") as r:
        json.dump(rarity_dict, r, indent=4, ensure_ascii=False)

    if num == 0:
        raise RuntimeError("Fail to classisy characters by rarity.")
    else:
        print(f"Done: Rarity classification ({num})")


def run(lang: str):
    _chars = _character()
    profession(_chars)
    rarity(_chars, lang)


if __name__ == "__main__":
    chars = _character()
    rarity(chars)

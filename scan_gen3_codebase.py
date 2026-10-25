import os
import re
from collections import defaultdict

EMERALD_DIR = r"C:\Users\Giovanni\Desktop\Emerald"

GEN3_SPECIES = [
    "TREECKO", "GROVYLE", "SCEPTILE", "TORCHIC", "COMBUSKEN", "BLAZIKEN",
    "MUDKIP", "MARSHTOMP", "SWAMPERT", "POOCHYENA", "MIGHTYENA", "ZIGZAGOON",
    "LINOONE", "WURMPLE", "SILCOON", "BEAUTIFLY", "CASCOON", "DUSTOX",
    "LOTAD", "LOMBRE", "LUDICOLO", "SEEDOT", "NUZLEAF", "SHIFTRY",
    "TAILLOW", "SWELLOW", "WINGULL", "PELIPPER", "RALTS", "KIRLIA",
    "GARDEVOIR", "SURSKIT", "MASQUERAIN", "SHROOMISH", "BRELOOM", "SLAKOTH",
    "VIGOROTH", "SLAKING", "NINCADA", "NINJASK", "SHEDINJA", "WHISMUR",
    "LOUDRED", "EXPLOUD", "MAKUHITA", "HARIYAMA", "AZURILL", "NOSEPASS",
    "SKITTY", "DELCATTY", "SABLEYE", "MAWILE", "ARON", "LAIRON",
    "AGGRON", "MEDITITE", "MEDICHAM", "ELECTRIKE", "MANECTRIC", "PLUSLE",
    "MINUN", "VOLBEAT", "ILLUMISE", "ROSELIA", "GULPIN", "SWALOT",
    "CARVANHA", "SHARPEDO", "WAILMER", "WAILORD", "NUMEL", "CAMERUPT",
    "TORKOAL", "SPOINK", "GRUMPIG", "SPINDA", "TRAPINCH", "VIBRAVA",
    "FLYGON", "CACNEA", "CACTURNE", "SWABLU", "ALTARIA", "ZANGOOSE",
    "SEVIPER", "LUNATONE", "SOLROCK", "BARBOACH", "WHISCASH", "CORPHISH",
    "CRAWDAUNT", "BALTOY", "CLAYDOL", "LILEEP", "CRADILY", "ANORITH",
    "ARMALDO", "FEEBAS", "MILOTIC", "CASTFORM", "KECLEON", "SHUPPET",
    "BANETTE", "DUSKULL", "DUSCLOPS", "TROPIUS", "CHIMECHO", "ABSOL",
    "WYNAUT", "SNORUNT", "GLALIE", "SPHEAL", "SEALEO", "WALREIN",
    "CLAMPERL", "HUNTAIL", "GOREBYSS", "RELICANTH", "LUVDISC", "BAGON",
    "SHELGON", "SALAMENCE", "BELDUM", "METANG", "METAGROSS", "REGIROCK",
    "REGICE", "REGISTEEL", "LATIAS", "LATIOS", "KYOGRE", "GROUDON",
    "RAYQUAZA", "JIRACHI", "DEOXYS"
]

GEN3_PATTERN = re.compile(r"\bSPECIES_(" + "|".join(GEN3_SPECIES) + r")\b")

TARGET_DIRS = ["data", "src"]

def scan():
    results = defaultdict(list)
    total_occurrences = 0

    for target in TARGET_DIRS:
        start_dir = os.path.join(EMERALD_DIR, target)
        for root, dirs, files in os.walk(start_dir):
            for f in files:
                if f.endswith((".c", ".h", ".inc", ".s", ".party", ".json")):
                    full_path = os.path.join(root, f)
                    rel_path = os.path.relpath(full_path, EMERALD_DIR)
                    
                    try:
                        with open(full_path, "r", encoding="utf-8", errors="ignore") as fp:
                            content = fp.read()
                    except Exception as e:
                        continue
                    
                    matches = GEN3_PATTERN.findall(content)
                    if matches:
                        results[rel_path] = matches
                        total_occurrences += len(matches)

    print(f"Total files with SPECIES_<GEN3>: {len(results)}")
    print(f"Total occurrences: {total_occurrences}\n")
    for path, matches in sorted(results.items(), key=lambda x: len(x[1]), reverse=True):
        print(f"{path}: {len(matches)} occurrences")

if __name__ == "__main__":
    scan()

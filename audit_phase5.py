import os
import re

EMERALD_DIR = r"C:\Users\Giovanni\Desktop\Emerald"

# Gen 3 species names to check for in event scripts, trades, and braille
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

PHASE5_FILES = [
    r"src\data\trade.h",
    r"src\braille_puzzles.c",
    r"data\maps\MirageTower_4F\scripts.inc",
    r"data\maps\DesertUnderpass\scripts.inc",
    r"data\maps\RustboroCity_DevonCorp_2F\scripts.inc",
    r"data\maps\MossdeepCity_StevensHouse\scripts.inc",
    r"data\maps\Route119_WeatherInstitute_2F\scripts.inc",
    r"data\maps\LavaridgeTown\scripts.inc",
    r"data\scripts\kecleon.inc",
    r"data\maps\FortreeCity\scripts.inc",
    r"data\maps\Route120\scripts.inc",
    r"data\maps\MarineCave_End\scripts.inc",
    r"data\maps\MarineCave_End\map.json",
    r"data\maps\TerraCave_End\scripts.inc",
    r"data\maps\TerraCave_End\map.json",
    r"data\maps\SkyPillar_Top\scripts.inc",
    r"data\maps\SkyPillar_Top\map.json",
    r"data\maps\DesertRuins\scripts.inc",
    r"data\maps\DesertRuins\map.json",
    r"data\maps\IslandCave\scripts.inc",
    r"data\maps\IslandCave\map.json",
    r"data\maps\AncientTomb\scripts.inc",
    r"data\maps\AncientTomb\map.json",
    r"data\maps\BirthIsland_Exterior\scripts.inc",
    r"data\maps\BirthIsland_Exterior\map.json",
    r"data\maps\SouthernIsland_Interior\scripts.inc",
    r"data\maps\SouthernIsland_Interior\map.json",
    r"data\maps\SootopolisCity\scripts.inc",
    r"data\maps\SeafloorCavern_Room9\scripts.inc",
    r"data\maps\SeafloorCavern_Room9\map.json",
    r"data\maps\MagmaHideout_4F\scripts.inc",
    r"data\maps\MagmaHideout_4F\map.json",
]

def audit():
    print("=== AUDIT PHASE 5 FILES ===")
    total_issues = 0
    for rel_path in PHASE5_FILES:
        full_path = os.path.join(EMERALD_DIR, rel_path)
        if not os.path.exists(full_path):
            print(f"[MISSING] {rel_path}")
            total_issues += 1
            continue
        
        with open(full_path, "r", encoding="utf-8", errors="ignore") as f:
            content = f.read()

        # Check for any SPECIES_<GEN3>
        found_gen3 = []
        for mon in GEN3_SPECIES:
            pattern = rf"\bSPECIES_{mon}\b"
            matches = re.findall(pattern, content)
            if matches:
                found_gen3.append((mon, len(matches)))
        
        # Check for OBJ_EVENT_GFX_SPECIES(<GEN3>) or OBJ_EVENT_GFX_SPECIES_<GEN3>
        found_gfx = []
        for mon in GEN3_SPECIES:
            pattern = rf"\bOBJ_EVENT_GFX_(?:SPECIES\({mon}\)|SPECIES_{mon}|{mon})\b"
            matches = re.findall(pattern, content)
            if matches:
                # filter out false positives like OBJ_EVENT_GFX_ITEM_BALL
                found_gfx.append((mon, len(matches)))
        
        if found_gen3 or found_gfx:
            print(f"[ISSUE] {rel_path}:")
            if found_gen3:
                print(f"   Gen 3 Species: {found_gen3}")
            if found_gfx:
                print(f"   Gen 3 GFX: {found_gfx}")
            total_issues += len(found_gen3) + len(found_gfx)
        else:
            print(f"[OK] {rel_path} - Clean!")

    print(f"\nTotal Issues Found: {total_issues}")

if __name__ == "__main__":
    audit()

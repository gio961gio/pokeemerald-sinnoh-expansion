import os
import json
import re
import sys

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

GEN3_SET = set(GEN3_SPECIES)
SPECIES_REGEX = re.compile(r"\bSPECIES_(" + "|".join(GEN3_SPECIES) + r")\b")

def audit_wild_encounters():
    path = os.path.join(EMERALD_DIR, "src", "data", "wild_encounters.json")
    with open(path, "r", encoding="utf-8") as f:
        data = json.load(f)
    
    issues = []
    total_slots = 0
    gen4_slots = 0
    
    def check_slots(group):
        nonlocal total_slots, gen4_slots
        for entry in group:
            for enc_type in ["land_mons", "water_mons", "rock_smash_mons", "fishing_mons"]:
                if enc_type in entry:
                    mons = entry[enc_type].get("mons", [])
                    for m in mons:
                        total_slots += 1
                        sp = m.get("species", "").replace("SPECIES_", "")
                        if sp in GEN3_SET:
                            issues.append(f"Wild encounter: {sp} in {entry.get('map')}")
    
    groups = data.get("wild_encounter_groups", [])
    if isinstance(groups, list):
        for v in groups:
            if "encounters" in v:
                check_slots(v["encounters"])
    elif isinstance(groups, dict):
        for k, v in groups.items():
            if "encounters" in v:
                check_slots(v["encounters"])
            
    return issues, total_slots

def audit_trainers():
    path = os.path.join(EMERALD_DIR, "src", "data", "trainers.party")
    with open(path, "r", encoding="utf-8") as f:
        text = f.read()
    matches = SPECIES_REGEX.findall(text)
    return [f"Trainer party: {m}" for m in matches]

def audit_battle_partners():
    path = os.path.join(EMERALD_DIR, "src", "data", "battle_partners.party")
    with open(path, "r", encoding="utf-8") as f:
        text = f.read()
    matches = SPECIES_REGEX.findall(text)
    return [f"Battle partner: {m}" for m in matches]

def audit_scripts():
    maps_dir = os.path.join(EMERALD_DIR, "data", "maps")
    issues = []
    for root, dirs, files in os.walk(maps_dir):
        for f in files:
            if f.endswith(".inc"):
                p = os.path.join(root, f)
                with open(p, "r", encoding="utf-8", errors="ignore") as fp:
                    content = fp.read()
                matches = SPECIES_REGEX.findall(content)
                if matches:
                    rel = os.path.relpath(p, maps_dir)
                    issues.append(f"Script {rel}: {len(matches)} matches ({set(matches)})")
    return issues

def audit_trades():
    path = os.path.join(EMERALD_DIR, "src", "data", "trade.h")
    with open(path, "r", encoding="utf-8") as f:
        text = f.read()
    matches = SPECIES_REGEX.findall(text)
    return [f"Trade.h: {m}" for m in matches]

def audit_species_enabled():
    path = os.path.join(EMERALD_DIR, "include", "config", "species_enabled.h")
    with open(path, "r", encoding="utf-8") as f:
        text = f.read()
    issues = []
    if not re.search(r"#define\s+P_GEN_3_POKEMON\s+FALSE", text):
        issues.append("P_GEN_3_POKEMON is not FALSE")
    if not re.search(r"#define\s+P_GEN_4_POKEMON\s+TRUE", text):
        issues.append("P_GEN_4_POKEMON is not TRUE")
    return issues

def audit_rom():
    rom_path = os.path.join(EMERALD_DIR, "pokeemerald.gba")
    if not os.path.exists(rom_path):
        return ["pokeemerald.gba not found"]
    size = os.path.getsize(rom_path)
    if size != 33554432:
        return [f"pokeemerald.gba invalid size: {size} bytes (expected 33554432)"]
    return []

def run_all():
    print("=" * 60)
    print("POKÉMON EMERALD -> SINNOH (GEN 4) AUDIT GENERALE")
    print("=" * 60)
    
    total_issues = 0
    
    # 1. Species enabled
    issues = audit_species_enabled()
    total_issues += len(issues)
    print(f"[*] species_enabled.h: {len(issues)} issues")
    for i in issues: print("    ", i)
    
    # 2. Wild encounters
    issues, slots = audit_wild_encounters()
    total_issues += len(issues)
    print(f"[*] wild_encounters.json ({slots} slots checked): {len(issues)} issues")
    for i in issues[:5]: print("    ", i)
    
    # 3. Trainers party
    issues = audit_trainers()
    total_issues += len(issues)
    print(f"[*] trainers.party: {len(issues)} issues")
    for i in issues[:5]: print("    ", i)
    
    # 4. Battle partners
    issues = audit_battle_partners()
    total_issues += len(issues)
    print(f"[*] battle_partners.party: {len(issues)} issues")
    for i in issues[:5]: print("    ", i)
    
    # 5. Trades
    issues = audit_trades()
    total_issues += len(issues)
    print(f"[*] trade.h: {len(issues)} issues")
    for i in issues[:5]: print("    ", i)
    
    # 6. Map scripts
    issues = audit_scripts()
    total_issues += len(issues)
    print(f"[*] data/maps scripts.inc: {len(issues)} issues")
    for i in issues[:5]: print("    ", i)
    
    # 7. ROM
    issues = audit_rom()
    total_issues += len(issues)
    print(f"[*] pokeemerald.gba binary: {len(issues)} issues")
    for i in issues: print("    ", i)
    
    print("-" * 60)
    print(f"TOTAL AUDIT ISSUES: {total_issues}")
    print("=" * 60)
    return total_issues

if __name__ == "__main__":
    run_all()

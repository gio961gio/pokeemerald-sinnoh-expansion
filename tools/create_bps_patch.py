#!/usr/bin/env python3
"""
Create a standard BPS (Beat Patch System) patch from a vanilla Pokémon Emerald ROM
to the compiled pokeemerald.gba (Sinnoh Edition).

Usage:
    python tools/create_bps_patch.py [vanilla_emerald.gba] [output_patch.bps]
"""

import sys
import os
import zlib
import struct

def encode_number(val: int) -> bytes:
    """Encode an integer using variable-length quantity encoding as specified by BPS."""
    res = bytearray()
    while True:
        b = val & 0x7F
        val >>= 7
        if val == 0:
            res.append(0x80 | b)
            break
        res.append(b)
        val -= 1
    return bytes(res)

def create_bps_patch(source_path: str, target_path: str, patch_path: str):
    if not os.path.exists(source_path):
        print(f"[-] Errore: File ROM Vanilla non trovato in: {source_path}")
        return False
    if not os.path.exists(target_path):
        print(f"[-] Errore: File ROM Moddata non trovato in: {target_path}")
        return False

    with open(source_path, "rb") as f:
        src = f.read()
    with open(target_path, "rb") as f:
        tgt = f.read()

    src_len = len(src)
    tgt_len = len(tgt)
    src_crc = zlib.crc32(src) & 0xFFFFFFFF
    tgt_crc = zlib.crc32(tgt) & 0xFFFFFFFF

    print(f"[*] Creazione patch BPS:")
    print(f"    - Sorgente: {source_path} ({src_len:,} byte, CRC32: {src_crc:08X})")
    print(f"    - Destinazione: {target_path} ({tgt_len:,} byte, CRC32: {tgt_crc:08X})")

    out = bytearray(b"BPS1")
    out += encode_number(src_len)
    out += encode_number(tgt_len)
    out += encode_number(0)  # metadata length = 0

    # Semplice algoritmo di patching BPS: SourceRead / TargetRead
    # BPS Actions:
    # 0 = SourceRead (lunghezza - 1)
    # 1 = TargetRead (lunghezza - 1) + bytes
    # 2 = SourceCopy
    # 3 = TargetCopy

    src_ptr = 0
    tgt_ptr = 0

    while tgt_ptr < tgt_len:
        # Trova blocchi identici con la sorgente
        match_len = 0
        while (src_ptr + match_len < src_len and 
               tgt_ptr + match_len < tgt_len and 
               src[src_ptr + match_len] == tgt[tgt_ptr + match_len]):
            match_len += 1

        if match_len > 0:
            # Emetti SourceRead
            data = ((match_len - 1) << 2) | 0
            out += encode_number(data)
            src_ptr += match_len
            tgt_ptr += match_len
            continue

        # Altrimenti trova la lunghezza del blocco di differenze
        diff_len = 0
        while (tgt_ptr + diff_len < tgt_len):
            if (src_ptr + diff_len < src_len and 
                src[src_ptr + diff_len] == tgt[tgt_ptr + diff_len]):
                # Se troviamo almeno 8 byte consecutivi uguali, interrompiamo TargetRead
                if diff_len >= 8 and src[src_ptr + diff_len:src_ptr + diff_len + 8] == tgt[tgt_ptr + diff_len:tgt_ptr + diff_len + 8]:
                    break
            diff_len += 1

        if diff_len > 0:
            data = ((diff_len - 1) << 2) | 1
            out += encode_number(data)
            out += tgt[tgt_ptr:tgt_ptr + diff_len]
            src_ptr += diff_len
            tgt_ptr += diff_len

    # Calcola il CRC della patch stessa (esclusi gli ultimi 4 byte di checksum patch)
    patch_body_crc = zlib.crc32(out + struct.pack("<II", src_crc, tgt_crc)) & 0xFFFFFFFF

    out += struct.pack("<III", src_crc, tgt_crc, patch_body_crc)

    with open(patch_path, "wb") as f:
        f.write(out)

    print(f"[+] Patch creata con successo in: {patch_path} ({len(out):,} byte)")
    return True

if __name__ == "__main__":
    src_file = sys.argv[1] if len(sys.argv) > 1 else "Pokemon - Emerald Version (USA, Europe).gba"
    tgt_file = sys.argv[2] if len(sys.argv) > 2 else "pokeemerald.gba"
    out_patch = sys.argv[3] if len(sys.argv) > 3 else "Pokemon_Emerald_Sinnoh_Edition.bps"
    create_bps_patch(src_file, tgt_file, out_patch)

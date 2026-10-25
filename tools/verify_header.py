import struct

with open('C:/Users/Giovanni/Desktop/Emerald/pokeemerald.gba', 'rb') as f:
    header = f.read(0xC0)

title = header[0xA0:0xAC].decode('latin1', errors='replace').rstrip('\x00')
game_code = header[0xAC:0xB0].decode('latin1', errors='replace')
maker_code = header[0xB0:0xB2].decode('latin1', errors='replace')
fixed_val = header[0xB2]
version = header[0xBC]
complement_check = header[0xBD]

chk = 0
for b in header[0xA0:0xBD]:
    chk = (chk - b) & 0xFF
chk = (chk - 0x19) & 0xFF

print('GBA ROM Header Verification:')
print(f'  Game Title:       "{title}"')
print(f'  Game Code:        "{game_code}"')
print(f'  Maker Code:       "{maker_code}"')
print(f'  Fixed Value 0x96: 0x{fixed_val:02X} (Valid: {fixed_val == 0x96})')
print(f'  Version:          v1.{version}')
print(f'  Complement Check: 0x{complement_check:02X} (Calculated: 0x{chk:02X}, Match: {complement_check == chk})')

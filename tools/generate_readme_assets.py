#!/usr/bin/env python3
import os
from PIL import Image, ImageDraw, ImageFont

BASE_DIR = r"c:\Users\Giovanni\Desktop\Emerald"
OUT_DIR = os.path.join(BASE_DIR, "docs", "images")
os.makedirs(OUT_DIR, exist_ok=True)

def get_frames(mon_path):
    img = Image.open(mon_path).convert("RGBA")
    w, h = img.size
    frame_h = 64
    f0 = img.crop((0, 0, 64, 64))
    f1 = img.crop((0, 64, 64, 128)) if h >= 128 else f0.copy()
    
    def strip_bg(frame):
        datas = frame.getdata()
        bg = datas[0]
        new_data = []
        for p in datas:
            if abs(p[0]-bg[0]) < 10 and abs(p[1]-bg[1]) < 10 and abs(p[2]-bg[2]) < 10:
                new_data.append((0, 0, 0, 0))
            else:
                new_data.append(p)
        frame.putdata(new_data)
        return frame
    
    return strip_bg(f0), strip_bg(f1)

def create_starters_gif():
    mons = [
        ("turtwig", "TURTWIG", "#48A048", "GRASS"),
        ("chimchar", "CHIMCHAR", "#F05030", "FIRE"),
        ("piplup", "PIPLUP", "#3890E8", "WATER"),
    ]
    
    frames_anim = []
    for step in range(4):
        # 4 frames in loop: f0, f1, f0, f1
        canvas = Image.new("RGBA", (660, 200), (20, 24, 33, 255))
        draw = ImageDraw.Draw(canvas)
        
        # Draw header
        draw.text((20, 15), "SINNOH STARTERS - PROF. BIRCH'S BAG", fill=(240, 240, 245))
        
        for idx, (folder, name, color, ptype) in enumerate(mons):
            x_offset = 20 + idx * 215
            # Card background
            draw.rounded_rectangle([x_offset, 45, x_offset + 195, 185], radius=8, fill=(30, 36, 48, 255), outline=(50, 60, 80, 255), width=2)
            
            # Badge
            draw.rounded_rectangle([x_offset + 10, 55, x_offset + 85, 75], radius=4, fill=color)
            draw.text((x_offset + 18, 58), ptype, fill=(255, 255, 255))
            draw.text((x_offset + 95, 58), name, fill=(230, 235, 245))
            
            # Sprite
            f0, f1 = get_frames(os.path.join(BASE_DIR, "graphics", "pokemon", folder, "anim_front.png"))
            frame = f1 if step % 2 == 1 else f0
            scaled = frame.resize((96, 96), Image.NEAREST)
            canvas.alpha_composite(scaled, (x_offset + 50, 82))
            
        frames_anim.append(canvas.convert("RGB"))
        
    out_path = os.path.join(OUT_DIR, "sinnoh_starters.gif")
    frames_anim[0].save(out_path, save_all=True, append_images=frames_anim[1:], duration=350, loop=0)
    print(f"[+] Saved starters GIF to {out_path}")

def create_legendaries_gif():
    mons = [
        ("dialga", "DIALGA", "TEMPORAL CAVE"),
        ("palkia", "PALKIA", "SPATIAL CAVE"),
        ("giratina/origin", "GIRATINA", "SKY PILLAR"),
        ("darkrai", "DARKRAI", "SOUTHERN ISLAND"),
        ("arceus", "ARCEUS", "BIRTH ISLAND"),
    ]
    
    frames_anim = []
    for step in range(4):
        canvas = Image.new("RGBA", (780, 190), (16, 18, 26, 255))
        draw = ImageDraw.Draw(canvas)
        draw.text((20, 12), "LEGENDARY ENCOUNTERS - GODS & TITANS OF SINNOH", fill=(240, 240, 245))
        
        for idx, (folder, name, loc) in enumerate(mons):
            x_offset = 15 + idx * 152
            draw.rounded_rectangle([x_offset, 38, x_offset + 142, 178], radius=6, fill=(26, 30, 42, 255), outline=(45, 52, 72, 255), width=1)
            draw.text((x_offset + 10, 46), name, fill=(255, 215, 0))
            draw.text((x_offset + 10, 62), loc, fill=(160, 170, 190))
            
            f0, f1 = get_frames(os.path.join(BASE_DIR, "graphics", "pokemon", folder, "anim_front.png"))
            frame = f1 if step % 2 == 1 else f0
            scaled = frame.resize((84, 84), Image.NEAREST)
            canvas.alpha_composite(scaled, (x_offset + 28, 85))
            
        frames_anim.append(canvas.convert("RGB"))
        
    out_path = os.path.join(OUT_DIR, "sinnoh_legendaries.gif")
    frames_anim[0].save(out_path, save_all=True, append_images=frames_anim[1:], duration=350, loop=0)
    print(f"[+] Saved legendaries GIF to {out_path}")

def create_hero_banner():
    canvas = Image.new("RGBA", (860, 260), (15, 17, 23, 255))
    draw = ImageDraw.Draw(canvas)
    
    # Outer decorative border
    draw.rounded_rectangle([10, 10, 850, 250], radius=12, fill=(22, 26, 36, 255), outline=(60, 80, 115, 255), width=2)
    
    # Titles
    draw.text((40, 30), "POKÉMON EMERALD: SINNOH EXPANSION", fill=(255, 255, 255))
    draw.text((40, 58), "A Complete Generation 4 Overhaul of Pokémon Emerald Version", fill=(96, 175, 255))
    draw.text((40, 85), "• 100% of Generation 3 Replaced (#252 - #386 Removed)", fill=(190, 200, 220))
    draw.text((40, 105), "• All 107 Sinnoh Pokémon (#387 - #493) Seamlessly Integrated", fill=(190, 200, 220))
    draw.text((40, 125), "• Physical/Special Move Split + Modern Gen 4 Battle Engine", fill=(190, 200, 220))
    draw.text((40, 145), "• 856 Reworked Trainer Teams • 6,459 Updated Wild Slots", fill=(190, 200, 220))
    draw.text((40, 165), "• Full Battle Frontier, Contests, Gyms & Elite Four Overhaul", fill=(190, 200, 220))
    draw.text((40, 200), "STATUS: GOLD MASTER v1.0.0 | FULL GBA DECOMPILATION", fill=(72, 200, 120))
    
    # Right showcase sprites
    showcase = ["turtwig", "chimchar", "piplup", "garchomp", "lucario"]
    positions = [(570, 40), (660, 30), (750, 45), (590, 130), (700, 120)]
    for mon, (x, y) in zip(showcase, positions):
        f0, _ = get_frames(os.path.join(BASE_DIR, "graphics", "pokemon", mon, "anim_front.png"))
        scaled = f0.resize((80, 80), Image.NEAREST)
        canvas.alpha_composite(scaled, (x, y))
        
    out_path = os.path.join(OUT_DIR, "banner.png")
    canvas.save(out_path)
    print(f"[+] Saved hero banner to {out_path}")

if __name__ == "__main__":
    create_starters_gif()
    create_legendaries_gif()
    create_hero_banner()

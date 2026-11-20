#!/usr/bin/env python3
"""Render entry.png: a newspaper front page for Friday 20 November 2026.

Every word is drawn with PIL so the lettering is exact. The five stories
were checked against news reports dated 20 November 2026; see README.md
for the source of each story.
"""
from PIL import Image, ImageDraw, ImageFont

PAGE_W, PAGE_H = 1024, 1024
PAPER = (250, 246, 234)
NAVY = (20, 33, 61)
NAVY_LIGHT = (52, 76, 120)
CRIMSON = (176, 32, 32)
GOLD = (235, 186, 78)
INK = (28, 28, 28)
MUTED = (96, 96, 90)
RULE = (158, 148, 126)

FONT_DIR = "/usr/share/fonts/truetype/dejavu/"
SERIF_BOLD = FONT_DIR + "DejaVuSerif-Bold.ttf"
SANS_BOLD = FONT_DIR + "DejaVuSans-Bold.ttf"
SANS_PLAIN = FONT_DIR + "DejaVuSans.ttf"


def load(path, size):
    return ImageFont.truetype(path, size)


def wrap_text(draw, text, fnt, max_width):
    """Split text into lines that fit max_width pixels (greedy)."""
    out, current = [], ""
    for word in text.split():
        candidate = (current + " " + word).strip()
        if draw.textlength(candidate, font=fnt) <= max_width:
            current = candidate
        else:
            if current:
                out.append(current)
            current = word
    if current:
        out.append(current)
    return out


def paragraph(draw, x, y, text, fnt, color, max_width, leading):
    """Draw a wrapped paragraph; return the y below its last line."""
    for line in wrap_text(draw, text, fnt, max_width):
        draw.text((x, y), line, font=fnt, fill=color)
        y += leading
    return y


def headline(draw, x, y, text, fnt, color, max_width, leading):
    """Draw a wrapped headline; return the y below it."""
    return paragraph(draw, x, y, text, fnt, color, max_width, leading)


# ------------------------------------------------------------- illustrations

def draw_cyclone(d, x, y, w, h):
    """Storm spiral over a dark sea, with rain and a sandy shore."""
    d.rectangle([x, y, x + w, y + h], fill=(30, 78, 122))
    cx, cy = x + w // 2, y + h // 2 - 6
    for radius in range(14, 72, 12):
        d.arc([cx - radius, cy - radius, cx + radius, cy + radius],
              start=30 + radius * 3, end=320 + radius * 3,
              fill=(240, 244, 248), width=7)
    d.ellipse([cx - 11, cy - 11, cx + 11, cy + 11], fill=GOLD)
    for rx, ry in [(x + 20, y + 16), (x + 52, y + 46), (x + w - 44, y + 20),
                   (x + w - 66, y + 58), (x + w - 24, y + 78)]:
        d.line([rx, ry, rx - 6, ry + 16], fill=(180, 210, 234), width=3)
    d.polygon([(x, y + h), (x, y + h - 30), (x + 78, y + h - 44),
               (x + 158, y + h - 24), (x + w, y + h - 38), (x + w, y + h)],
              fill=(198, 166, 112))
    d.rectangle([x, y + h - 8, x + w, y + h], fill=(150, 122, 78))


def draw_kyiv(d, x, y, w, h):
    """Night skyline with domes, a missile streak and an explosion burst."""
    d.rectangle([x, y, x + w, y + h], fill=(14, 18, 44))
    for sx, sy in [(x + 18, y + 14), (x + 58, y + 30), (x + 120, y + 12),
                   (x + w - 30, y + 24), (x + w - 70, y + 44)]:
        d.ellipse([sx - 2, sy - 2, sx + 2, sy + 2], fill=(255, 255, 255))
    # missile streak from the top right
    d.line([x + w - 16, y + 8, x + w - 78, y + 62], fill=(255, 190, 60),
           width=4)
    d.line([x + w - 30, y + 4, x + w - 88, y + 54], fill=(255, 230, 150),
           width=2)
    base = y + h - 26
    # buildings with lit windows
    for bx, bw, bh in [(0, 30, 62), (34, 26, 88), (64, 32, 70),
                       (100, 28, 96), (132, 30, 60)]:
        d.rectangle([x + bx, base - bh, x + bx + bw, base], fill=(38, 44, 78))
        for wy in range(base - bh + 10, base - 8, 16):
            for wx in range(x + bx + 6, x + bx + bw - 6, 12):
                d.rectangle([wx, wy, wx + 5, wy + 7], fill=(255, 214, 120))
    # golden dome in the middle
    d.pieslice([x + 66, base - 118, x + 98, base - 86], 180, 360,
               fill=GOLD)
    d.rectangle([x + 80, base - 128, x + 84, base - 116], fill=GOLD)
    # explosion burst on the right-hand building
    ex, ey = x + 146, base - 78
    for angle in range(0, 360, 30):
        import math
        tip_x = ex + int(22 * math.cos(math.radians(angle)))
        tip_y = ey + int(22 * math.sin(math.radians(angle)))
        d.line([ex, ey, tip_x, tip_y], fill=(255, 140, 40), width=3)
    d.ellipse([ex - 9, ey - 9, ex + 9, ey + 9], fill=(255, 220, 90))
    d.rectangle([x, base, x + w, y + h], fill=(22, 22, 34))


def draw_calendar(d, x, y, w, h):
    """A wall calendar turned to 2027, with a pause mark for the delay."""
    d.rectangle([x, y, x + w, y + h], fill=(228, 232, 240))
    d.rectangle([x + 18, y + 16, x + w - 18, y + h - 14], fill=(255, 255, 255),
                outline=(120, 128, 140), width=2)
    d.rectangle([x + 18, y + 16, x + w - 18, y + 52], fill=CRIMSON)
    d.text((x + w // 2, y + 22), "2027", font=load(SANS_BOLD, 26),
           fill=(255, 255, 255), anchor="ma")
    # calendar grid dots
    for row in range(3):
        for col in range(5):
            gx = x + 44 + col * 22
            gy = y + 68 + row * 22
            d.ellipse([gx - 5, gy - 5, gx + 5, gy + 5],
                      fill=(52, 76, 120) if (row, col) != (1, 2) else CRIMSON)
    # pause bars on the right
    px = x + w - 52
    d.rectangle([px, y + 66, px + 10, y + 118], fill=NAVY)
    d.rectangle([px + 16, y + 66, px + 26, y + 118], fill=NAVY)
    d.text((x + w // 2, y + h - 30), "NOT YET", font=load(SANS_BOLD, 16),
           fill=CRIMSON, anchor="ma")


def draw_tower(d, x, y, w, h):
    """A tall glass tower with a band of damaged, darkened floors."""
    d.rectangle([x, y, x + w, y + h], fill=(196, 214, 230))
    d.rectangle([x, y + h - 20, x + w, y + h], fill=(90, 96, 104))
    tx, tw = x + 52, 68
    d.rectangle([tx, y + 10, tx + tw, y + h - 20], fill=(52, 76, 120))
    # window grid; the damaged band is dark with jagged edges
    for row in range(9):
        wy = y + 18 + row * 13
        for col in range(4):
            wx = tx + 8 + col * 15
            if row in (3, 4):
                d.rectangle([wx, wy, wx + 10, wy + 8], fill=(30, 30, 30))
            else:
                d.rectangle([wx, wy, wx + 10, wy + 8], fill=(168, 208, 236))
    # jagged crack through the damaged band
    d.line([(tx - 4, y + 58), (tx + 18, y + 66), (tx + 34, y + 58),
            (tx + 52, y + 68), (tx + tw + 4, y + 60)],
           fill=(255, 220, 90), width=3)
    # smaller neighbours
    d.rectangle([x + 8, y + 66, x + 38, y + h - 20], fill=(90, 110, 140))
    d.rectangle([x + w - 40, y + 84, x + w - 10, y + h - 20],
                fill=(90, 110, 140))
    d.ellipse([x + w - 34, y + 14, x + w - 14, y + 34], fill=GOLD)


def draw_globe(d, x, y, w, h):
    """A globe with green land, a rising sun and a small leaf."""
    d.rectangle([x, y, x + w, y + h], fill=(214, 232, 240))
    cx, cy, r = x + w // 2 - 6, y + h // 2 + 4, 58
    d.ellipse([cx - r, cy - r, cx + r, cy + r], fill=(70, 140, 200))
    d.ellipse([cx - 34, cy - 40, cx + 6, cy - 6], fill=(96, 178, 92))
    d.ellipse([cx - 6, cy + 8, cx + 40, cy + 44], fill=(96, 178, 92))
    d.ellipse([cx + 18, cy - 34, cx + 46, cy - 8], fill=(120, 190, 110))
    d.arc([cx - r, cy - r, cx + r, cy + r], 0, 360, fill=NAVY, width=3)
    # sun in the corner
    sx, sy = x + w - 30, y + 24
    d.ellipse([sx - 12, sy - 12, sx + 12, sy + 12], fill=GOLD)
    for angle in range(0, 360, 45):
        import math
        d.line([sx + int(16 * math.cos(math.radians(angle))),
                sy + int(16 * math.sin(math.radians(angle))),
                sx + int(24 * math.cos(math.radians(angle))),
                sy + int(24 * math.sin(math.radians(angle)))],
               fill=GOLD, width=3)
    # leaf at the base
    d.pieslice([x + 14, y + h - 44, x + 46, y + h - 12], 270, 90,
               fill=(70, 150, 80))
    d.line([x + 16, y + h - 16, x + 42, y + h - 40], fill=(40, 110, 50),
           width=2)


# ------------------------------------------------------------------- page

img = Image.new("RGB", (PAGE_W, PAGE_H), PAPER)
d = ImageDraw.Draw(img)

# masthead
d.rectangle([0, 0, PAGE_W, 118], fill=NAVY)
d.text((512, 8), "THE WORLD IN ONE DAY", font=load(SERIF_BOLD, 34),
       fill=(255, 255, 255), anchor="ma")
d.text((512, 54), "FRIDAY, 20 NOVEMBER 2026", font=load(SANS_BOLD, 38),
       fill=GOLD, anchor="ma")
d.rectangle([0, 118, PAGE_W, 126], fill=CRIMSON)

# ---------------------------------------------------------------- lead story
LEAD_Y, LEAD_H = 140, 258
d.rectangle([16, LEAD_Y, PAGE_W - 16, LEAD_Y + LEAD_H], outline=RULE, width=2)
draw_cyclone(d, 28, LEAD_Y + 12, 372, 234)
lead_x = 424
lead_head = "CYCLONE AKVAN MAKES LANDFALL"
head_y = headline(d, lead_x, LEAD_Y + 12, lead_head, load(SANS_BOLD, 30),
                  NAVY, 560, 36)
lead_body = (
    "Cyclone Akvan crosses India's east coast near Gopalpur, Odisha, on "
    "Friday morning. More than 300,000 people have been evacuated and 423 "
    "rescue teams are on alert as winds gust to 90 km/h.")
paragraph(d, lead_x, head_y + 10, lead_body, load(SANS_PLAIN, 21), INK, 560,
          27)
d.text((lead_x, LEAD_Y + LEAD_H - 30), "INDIA  \u00b7  IMD",
       font=load(SANS_BOLD, 15), fill=MUTED)

# ---------------------------------------------------------------- story grid
stories = [
    ("MISSILES HIT KYIV OVERNIGHT",
     "Russia fires ballistic missiles at Kyiv in the early hours of Friday. "
     "Explosions rock the capital and a fire breaks out in a building in "
     "the Obolonskyi district after it is hit by missile debris.",
     draw_kyiv, "UKRAINE  \u00b7  REUTERS"),
    ("TRUMP PUTS IRAN DECISION OFF TO 2027",
     "President Trump says he is in no rush to order new strikes on Iran "
     "and will decide after the new year. The Senate votes 51-48 against "
     "limiting his war powers on Iran.",
     draw_calendar, "UNITED STATES  \u00b7  REUTERS"),
    ("HOUTHI STRIKE DAMAGES RIYADH TOWER",
     "Saudi Arabia confirms a Houthi missile strike damaged the PIF Tower, "
     "the Riyadh headquarters of its sovereign wealth fund. Windows are "
     "blown out across several floors; no injuries are reported.",
     draw_tower, "SAUDI ARABIA  \u00b7  REUTERS"),
    ("COP31 CLIMATE TALKS CLOSE IN ANTALYA",
     "The UN climate summit in Antalya, Turkiye, closes today. A draft text "
     "on fossil fuels and climate finance is still contested as the "
     "two-week conference ends.",
     draw_globe, "TURKIYE  \u00b7  UNFCCC"),
]

GRID_X, GRID_Y = 16, 414
CELL_W, CELL_H, GAP = 488, 272, 16
for i, (head, body, illo, tag) in enumerate(stories):
    cx = GRID_X + (i % 2) * (CELL_W + GAP)
    cy = GRID_Y + (i // 2) * (CELL_H + GAP)
    d.rectangle([cx, cy, cx + CELL_W, cy + CELL_H], outline=RULE, width=2)
    illo(d, cx + 12, cy + 12, 172, 150)
    tx = cx + 198
    end_y = headline(d, tx, cy + 12, head, load(SANS_BOLD, 22), NAVY, 276, 26)
    paragraph(d, tx, end_y + 6, body, load(SANS_PLAIN, 17), INK, 276, 21)
    d.text((tx, cy + CELL_H - 26), tag, font=load(SANS_BOLD, 13), fill=MUTED)

# ------------------------------------------------------------------- footer
d.rectangle([0, 978, PAGE_W, PAGE_H], fill=NAVY)
d.text((512, 986),
       "All five stories happened or were first reported on 20 November 2026  \u00b7  "
       "Sources: IMD, Reuters, BusinessWorld, UNFCCC",
       font=load(SANS_PLAIN, 15), fill=(222, 222, 212), anchor="ma")

img.save("entry.png", optimize=True)
print("saved entry.png", img.size)

#!/usr/bin/env python3
"""news-image-20261121: one front page summing up Saturday 21 November 2026.

Draws a 1024x1024 newspaper front page with PIL: masthead, a hero story
(Kryvyi Rih double-tap strike), four panels (COP31, Mexico, markets,
Baltic ship) and a footer strip (Gaza, dengue trial). No network, no
randomness, no clock: the same input always writes the same bytes.
"""
import os
import sys

from PIL import Image, ImageDraw, ImageFont

W, H = 1024, 1024
OUT_DEFAULT = "/output/entry.png"

PAPER = (247, 242, 231)
INK = (18, 18, 18)
RED = (178, 34, 34)
NAVY = (22, 35, 61)
NAVY2 = (30, 48, 82)
GOLD = (214, 158, 46)
TEAL = (14, 110, 110)
RUST = (166, 66, 28)
STEEL = (52, 92, 128)
DARKRED = (140, 28, 28)
CREAM = (247, 242, 231)
GREY = (90, 90, 86)
LIGHT = (233, 226, 210)

SERIF_B = "/usr/share/fonts/truetype/liberation/LiberationSerif-Bold.ttf"
SERIF = "/usr/share/fonts/truetype/liberation/LiberationSerif-Regular.ttf"
SANS_B = "/usr/share/fonts/truetype/liberation/LiberationSans-Bold.ttf"
SANS = "/usr/share/fonts/truetype/liberation/LiberationSans-Regular.ttf"


def font(path, size):
    return ImageFont.truetype(path, size)


def wrap(draw, text, fnt, max_w):
    words = text.split()
    lines, cur = [], ""
    for w in words:
        trial = (cur + " " + w).strip()
        if draw.textlength(trial, font=fnt) <= max_w:
            cur = trial
        else:
            if cur:
                lines.append(cur)
            cur = w
    if cur:
        lines.append(cur)
    return lines


def text_block(draw, x, y, lines, fnt, fill, leading):
    for ln in lines:
        draw.text((x, y), ln, font=fnt, fill=fill)
        y += leading
    return y


def draw_masthead(d):
    d.rectangle([0, 0, W, 118], fill=PAPER)
    f_title = font(SERIF_B, 74)
    title = "THE WORLD TODAY"
    tw = d.textlength(title, font=f_title)
    d.text(((W - tw) / 2, 8), title, font=f_title, fill=INK)
    d.rectangle([48, 96, W - 48, 99], fill=INK)
    f_date = font(SANS_B, 24)
    date = "SATURDAY, 21 NOVEMBER 2026"
    dw = d.textlength(date, font=f_date)
    d.text(((W - dw) / 2, 104), date, font=f_date, fill=RED)
    d.rectangle([48, 132, W - 48, 135], fill=INK)


def draw_hero(d):
    x0, y0, x1, y1 = 48, 150, W - 48, 512
    d.rectangle([x0, y0, x1, y1], fill=NAVY)
    # night sky stars
    stars = [(90, 180), (180, 168), (300, 190), (420, 172), (560, 186),
             (700, 170), (830, 188), (920, 175), (240, 210), (640, 205)]
    for sx, sy in stars:
        d.ellipse([sx, sy, sx + 3, sy + 3], fill=(200, 205, 220))
    # missile streaks, ending at the two impact fires
    d.line([(120, 210), (350, 320)], fill=GOLD, width=5)
    d.line([(880, 200), (710, 318)], fill=GOLD, width=5)
    # one continuous skyline across the whole hero, so no lit window
    # ever floats in empty sky; the two struck blocks stand lower
    base = y1 - 118
    buildings = [(48, 330, 105), (105, 300, 160), (160, 345, 215),
                 (215, 310, 275), (275, 348, 330), (330, 356, 395),
                 (395, 315, 455), (455, 340, 515), (515, 305, 575),
                 (575, 335, 635), (635, 348, 690), (690, 354, 750),
                 (750, 315, 810), (810, 340, 870), (870, 305, 930),
                 (930, 345, 976)]
    for bx, top, bx2 in buildings:
        d.rectangle([bx, top, bx2, base], fill=(10, 16, 30))
    # lit windows, only inside a building's own walls
    for bx, top, bx2 in buildings:
        for wx in range(bx + 10, bx2 - 8, 22):
            for wy in (top + 14, top + 40, top + 66):
                if wy + 8 < base - 4 and (wx * 7 + wy) % 5 == 0:
                    d.rectangle([wx, wy, wx + 6, wy + 8], fill=(255, 200, 90))
    # fires burning on the rooftops of the two struck blocks, with
    # smoke rising from each in a tapering column
    for cx, roof in [(362, 356), (720, 354)]:
        d.ellipse([cx - 34, roof - 16, cx + 34, roof + 10], fill=(255, 120, 30))
        d.ellipse([cx - 22, roof - 40, cx + 22, roof + 4], fill=(255, 120, 30))
        d.ellipse([cx - 12, roof - 28, cx + 12, roof + 2], fill=(255, 190, 60))
        d.ellipse([cx - 5, roof - 16, cx + 5, roof + 2], fill=(255, 230, 120))
        plume = [(cx - 8, roof - 76, cx + 16, roof - 44, (120, 120, 125)),
                 (cx + 0, roof - 102, cx + 20, roof - 70, (140, 140, 145)),
                 (cx + 8, roof - 124, cx + 24, roof - 94, (160, 160, 165))]
        for px0, py0, px1, py1, col in plume:
            d.ellipse([px0, py0, px1, py1], fill=col)
    # headline over the scene, bottom of hero
    d.rectangle([x0, y1 - 118, x1, y1], fill=(12, 18, 34))
    f_h = font(SERIF_B, 52)
    d.text((x0 + 20, y1 - 112), "DOUBLE-TAP ON KRYVYI RIH", font=f_h, fill=(255, 255, 255))
    f_s = font(SANS, 22)
    sub = ("Russian ballistic missiles hit Zelenskyy's hometown: a 7-year-old "
           "boy and a 20-year-old paramedic killed, 60 wounded \u2014 and "
           "rescuers struck as they worked.")
    lines = wrap(d, sub, f_s, x1 - x0 - 40)
    text_block(d, x0 + 20, y1 - 52, lines, f_s, (225, 225, 225), 27)


def draw_panel(d, x0, y0, x1, y1, band, kicker, headline, body, art):
    d.rectangle([x0, y0, x1, y1], fill=(255, 255, 255))
    d.rectangle([x0, y0, x1, y0 + 4], fill=band)
    d.rectangle([x0, y0, x1, y1], outline=(200, 195, 180), width=2)
    f_k = font(SANS_B, 19)
    d.text((x0 + 14, y0 + 14), kicker, font=f_k, fill=band)
    f_h = font(SERIF_B, 30)
    hl = wrap(d, headline, f_h, x1 - x0 - 28 - 84)
    y = text_block(d, x0 + 14, y0 + 42, hl, f_h, INK, 34)
    f_b = font(SANS, 20)
    bl = wrap(d, body, f_b, x1 - x0 - 28)
    text_block(d, x0 + 14, y + 6, bl, f_b, (60, 60, 60), 25)
    art(d, x1 - 52, y0 + 62, 30)


def art_cop(d, cx, cy, r):
    d.ellipse([cx - r, cy - r, cx + r, cy + r], fill=TEAL)
    d.ellipse([cx - r + 10, cy - r + 10, cx + r - 10, cy + r - 10],
              fill=(90, 190, 170))
    d.line([(cx - r, cy), (cx + r, cy)], fill=(255, 255, 255), width=3)
    d.ellipse([cx - r, cy - r, cx + r, cy + r], outline=(255, 255, 255), width=3)


def art_mexico(d, cx, cy, r):
    d.ellipse([cx - r, cy - r, cx + r, cy + r], fill=RUST)
    d.text((cx - 11, cy - 18), "$", font=font(SANS_B, 36), fill=(255, 255, 255))
    d.line([(cx - r, cy + 8), (cx + r, cy + 8)], fill=(255, 255, 255), width=3)


def art_markets(d, cx, cy, r):
    d.ellipse([cx - r, cy - r, cx + r, cy + r], fill=DARKRED)
    pts = [(cx - 20, cy - 5), (cx - 7, cy + 2), (cx + 5, cy - 9), (cx + 20, cy + 12)]
    d.line(pts, fill=(255, 255, 255), width=4)
    d.polygon([(cx + 20, cy + 12), (cx + 10, cy + 12), (cx + 20, cy + 2)],
              fill=(255, 255, 255))


def art_baltic(d, cx, cy, r):
    d.ellipse([cx - r, cy - r, cx + r, cy + r], fill=STEEL)
    d.polygon([(cx - 17, cy - 2), (cx + 17, cy - 2), (cx + 10, cy + 10),
               (cx - 10, cy + 10)], fill=(255, 255, 255))
    d.rectangle([cx - 3, cy - 16, cx + 3, cy - 2], fill=(255, 255, 255))
    d.line([(cx - 25, cy + 17), (cx - 8, cy + 12), (cx + 8, cy + 17),
            (cx + 25, cy + 12)], fill=(255, 255, 255), width=3)


def draw_footer(d):
    y0, y1 = 906, 1000
    d.rectangle([48, y0, W - 48, y1], fill=LIGHT)
    d.rectangle([48, y0, W - 48, y0 + 3], fill=INK)
    f_k = font(SANS_B, 19)
    f_b = font(SANS, 20)
    d.text((64, y0 + 12), "GAZA", font=f_k, fill=RED)
    gaza = "Six killed in Israeli strikes despite the ceasefire."
    d.text((64, y0 + 38), gaza, font=f_b, fill=INK)
    d.line([(512, y0 + 14), (512, y1 - 12)], fill=(180, 175, 160), width=2)
    d.text((532, y0 + 12), "HOPE IN BRAZIL", font=f_k, fill=TEAL)
    dengue = ("Wolbachia mosquitoes cut dengue and chikungunya 69% "
              "in a trial of 5,700 children.")
    dl = wrap(d, dengue, f_b, W - 48 - 532 - 16)
    text_block(d, 532, y0 + 38, dl, f_b, INK, 24)


def build():
    img = Image.new("RGB", (W, H), PAPER)
    d = ImageDraw.Draw(img)
    draw_masthead(d)
    draw_hero(d)
    gx0, gy0 = 48, 532
    pw, ph = 452, 172
    gap = 24
    panels = [
        (TEAL, "CLIMATE \u00b7 ANTALYA", "TALKS RUN OVER",
         "COP31 passes its deadline with no deal yet; the draft leaves out fossil fuels.",
         art_cop),
        (RUST, "MEXICO \u00b7 SINALOA", "EL CHAPO ISIDRO CAUGHT",
         "FBI most-wanted cartel boss seized overnight, with US intelligence help.",
         art_mexico),
        (DARKRED, "MARKETS \u00b7 WALL STREET", "AI SELL-OFF SINKS STOCKS",
         "S&P 500 -3.7%, Nasdaq -5.3%, Nvidia -14%, Nikkei -5.1% in the sell-off.",
         art_markets),
        (STEEL, "BALTIC SEA", "SHIP ABLAZE IN THE GULF",
         "Sanctioned Russian cargo ship Sparta II hit by drones off Finland, on fire.",
         art_baltic),
    ]
    for i, (band, kicker, head, body, art) in enumerate(panels):
        x0 = gx0 + (i % 2) * (pw + gap)
        y0 = gy0 + (i // 2) * (ph + gap)
        draw_panel(d, x0, y0, x0 + pw, y0 + ph, band, kicker, head, body, art)
    draw_footer(d)
    d.text((48, 1004), "", font=font(SANS, 10), fill=GREY)
    return img


def main(argv):
    out = argv[1] if len(argv) > 1 else OUT_DEFAULT
    img = build()
    parent = os.path.dirname(os.path.abspath(out))
    if parent:
        os.makedirs(parent, exist_ok=True)
    img.save(out, "JPEG", quality=92)
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))

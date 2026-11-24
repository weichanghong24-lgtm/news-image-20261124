#!/usr/bin/env python3
"""Build the make.fun news-image entry for 24 November 2026.

Renders a broadsheet front page ("THE WORLD IN ONE DAY") as a
1024x1024 PNG using Pillow only. No network access, no timestamps,
no randomness: repeated runs produce byte-identical output.
"""

import hashlib
import os
import textwrap

from PIL import Image, ImageDraw, ImageFont

W, H = 1024, 1024
OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "entry.png")

PAPER = (247, 243, 234)      # warm newsprint
INK = (24, 24, 24)           # near-black
RED = (176, 30, 36)          # broadsheet accent red
GREY = (96, 90, 82)          # muted grey-brown
RULE = (60, 56, 50)          # rule lines
PANEL = (238, 232, 219)      # hero panel fill
STRIP = (232, 226, 208)      # market strip fill

FONT_DIR = "/usr/share/fonts/truetype/dejavu"


def font(name, size):
    return ImageFont.truetype(os.path.join(FONT_DIR, name), size)


SERIF_B = lambda s: font("DejaVuSerif-Bold.ttf", s)     # noqa: E731
SERIF = lambda s: font("DejaVuSerif.ttf", s)            # noqa: E731
SANS_B = lambda s: font("DejaVuSans-Bold.ttf", s)       # noqa: E731
SANS = lambda s: font("DejaVuSans.ttf", s)              # noqa: E731
MONO_B = lambda s: font("DejaVuSansMono-Bold.ttf", s)   # noqa: E731


def wrap(draw, text, fnt, width):
    """Greedy word wrap of `text` to fit `width` pixels."""
    lines = []
    for para in text.split("\n"):
        words = para.split()
        if not words:
            lines.append("")
            continue
        cur = words[0]
        for w in words[1:]:
            trial = cur + " " + w
            if draw.textlength(trial, font=fnt) <= width:
                cur = trial
            else:
                lines.append(cur)
                cur = w
        lines.append(cur)
    return lines


def draw_wrapped(draw, x, y, text, fnt, width, fill=INK, leading=None):
    """Draw wrapped text; return y just below the last line."""
    if leading is None:
        leading = int(fnt.size * 1.28)
    for line in wrap(draw, text, fnt, width):
        draw.text((x, y), line, font=fnt, fill=fill)
        y += leading
    return y


def hrule(draw, x0, x1, y, width=2, fill=RULE):
    draw.line([(x0, y), (x1, y)], fill=fill, width=width)


def story(draw, x, y, width, kicker, headline, body, head_size=24):
    """One column story: red kicker, bold headline, small body text."""
    y = draw_wrapped(draw, x, y, kicker, SANS_B(15), width, fill=RED,
                     leading=19)
    y = draw_wrapped(draw, x, y + 3, headline, SERIF_B(head_size), width,
                     leading=int(head_size * 1.17))
    y = draw_wrapped(draw, x, y + 4, body, SANS(16), width, leading=20)
    return y


def main():
    img = Image.new("RGB", (W, H), PAPER)
    d = ImageDraw.Draw(img)
    mx = 36                      # side margin
    rx = W - mx                  # right edge

    # ---------- Masthead ----------
    title = "THE WORLD IN ONE DAY"
    tf = SERIF_B(58)
    tw = d.textlength(title, font=tf)
    d.text(((W - tw) / 2, 26), title, font=tf, fill=INK)
    date = "TUESDAY 24 NOVEMBER 2026  ·  WORLD NEWS IN ONE IMAGE"
    df = SANS_B(17)
    dw = d.textlength(date, font=df)
    d.text(((W - dw) / 2, 100), date, font=df, fill=GREY)
    hrule(d, mx, rx, 132, width=4)
    hrule(d, mx, rx, 138, width=1)

    # ---------- Hero panel ----------
    hy0, hy1 = 150, 340
    d.rectangle([mx, hy0, rx, hy1], fill=PANEL, outline=RULE, width=2)
    d.text((mx + 22, hy0 + 12), "TOP STORY", font=SANS_B(16), fill=RED)
    hero_head = "Houthi missile hits Riyadh's tallest tower"
    y = draw_wrapped(d, mx + 22, hy0 + 36, hero_head, SERIF_B(40),
                     rx - mx - 44, leading=47)
    hero_deck = ("Second strike in five days injures 11 people. "
                 "Houthi fighters are now reported about 60 km from Aden.")
    draw_wrapped(d, mx + 22, y + 6, hero_deck, SANS(19),
                 rx - mx - 44, fill=(52, 48, 44), leading=24)

    # ---------- Two columns of stories ----------
    col_y = 356
    col_w = (rx - mx - 28) // 2
    lx, rx2 = mx, mx + col_w + 28

    y = story(d, lx, col_y, col_w,
              "EUROPE",
              "Russia warns Estonia of \"open war\"",
              "Moscow threatens over Tallinn's plan to close border "
              "crossings on 1 December.")
    hrule(d, lx, lx + col_w, y + 10, width=1, fill=(170, 162, 148))
    y = story(d, lx, y + 22, col_w,
              "TECH",
              "Nvidia chief reinstated days after resigning",
              "Jensen Huang is back after Trump pushed for his return; "
              "Congress presses its China chip probe.")
    hrule(d, lx, lx + col_w, y + 10, width=1, fill=(170, 162, 148))
    y = story(d, lx, y + 22, col_w,
              "ASIA",
              "Magnitude 5.4 quake shakes Nepal",
              "Tremors from Koshi Province felt in India, Bhutan and "
              "Bangladesh.")

    y = story(d, rx2, col_y, col_w,
              "SPORT",
              "Senegal reinstated as Africa Cup champions",
              "Top sports court restores Senegal as 2025 Africa Cup of "
              "Nations winners.")
    hrule(d, rx2, rx2 + col_w, y + 10, width=1, fill=(170, 162, 148))
    y = story(d, rx2, y + 22, col_w,
              "DEFENCE",
              "NATO vows space defence",
              "Chief Mark Rutte pledges action after reports Russia is "
              "preparing a nuclear-armed satellite.")
    hrule(d, rx2, rx2 + col_w, y + 10, width=1, fill=(170, 162, 148))
    y = story(d, rx2, y + 22, col_w,
              "MIDDLE EAST",
              "Israeli strikes kill Hamas security chief",
              "Naeem Abu Nahel and six others killed in Gaza.")

    # ---------- Market strip ----------
    sy0, sy1 = 786, 852
    d.rectangle([mx, sy0, rx, sy1], fill=STRIP, outline=RULE, width=2)
    d.text((mx + 18, sy0 + 9), "MARKETS", font=SANS_B(15), fill=RED)
    stats = [("S&P 500", "-0.95%", RED),
             ("EURO STOXX 50", "-1.16%", RED),
             ("BRENT CRUDE", "$87.51  +0.96%", INK)]
    seg_w = (rx - mx - 150) // 3
    for i, (label, val, vc) in enumerate(stats):
        sx = mx + 150 + i * seg_w
        d.text((sx, sy0 + 10), label, font=SANS_B(15), fill=GREY)
        d.text((sx, sy0 + 32), val, font=MONO_B(22), fill=vc)

    # ---------- Bottom ticker ----------
    ty = 866
    d.text((mx, ty), "ALSO TODAY", font=SANS_B(15), fill=RED)
    hrule(d, mx, rx, ty + 22, width=1, fill=(170, 162, 148))
    ticker = (
        "Zaporizhzhia: 2 killed, 40 wounded  ·  700,000+ Russian soldiers "
        "killed, leaked data shows  ·  Hasina to return to Bangladesh 16 Dec  ·  "
        "EU sanctions hit Russian banks, soldiers, athletes  ·  China probes "
        "Politburo member Chen Jining  ·  Pentagon: Canada falls short as "
        "partner  ·  Iran vows to confront US naval blockade  ·  COP31 ends "
        "with no deal  ·  Spain amnesties Puigdemont  ·  Iraq takes Kurdish "
        "oilfields  ·  S. Korea: Russian jets in defence zone; $375,000 "
        "rewards vs AI exam cheating"
    )
    draw_wrapped(d, mx, ty + 30, ticker, SANS(15), rx - mx,
                 fill=(52, 48, 44), leading=20)

    # ---------- Footer ----------
    hrule(d, mx, rx, 992, width=1, fill=(170, 162, 148))
    foot = "Compiled from wire and press summaries  ·  24 November 2026"
    fw = d.textlength(foot, font=SANS(13))
    d.text(((W - fw) / 2, 999), foot, font=SANS(13), fill=GREY)

    img.save(OUT, format="PNG", optimize=True)
    size = os.path.getsize(OUT)
    sha = hashlib.sha256(open(OUT, "rb").read()).hexdigest()
    print(f"wrote {OUT}  {img.size[0]}x{img.size[1]}  {size} bytes")
    print(f"sha256: {sha}")


if __name__ == "__main__":
    main()

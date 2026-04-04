#!/usr/bin/env python3
"""Generiert images/og-image.png (1200x630) und images/favicon-32-dark.png für BERENT."""
from __future__ import annotations

import os
import sys
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont

ROOT = Path(__file__).resolve().parents[1]
IMAGES = ROOT / "images"
LOGO_PATH = IMAGES / "logo_kompakt_farbe_v3.png"

BG = "#090806"
COPPER = "#B5742A"
TEXT_MUTED = "#C4BCB1"


def load_font(size: int, bold: bool = False) -> ImageFont.FreeTypeFont | ImageFont.ImageFont:
    candidates = []
    if sys.platform == "darwin":
        candidates.extend(
            [
                "/System/Library/Fonts/Supplemental/Arial Bold.ttf" if bold else "/System/Library/Fonts/Supplemental/Arial.ttf",
                "/System/Library/Fonts/Helvetica.ttc",
                "/Library/Fonts/Arial.ttf",
            ]
        )
    candidates.extend(
        [
            "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf" if bold else "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf",
            "/usr/share/fonts/truetype/liberation/LiberationSans-Bold.ttf" if bold else "/usr/share/fonts/truetype/liberation/LiberationSans-Regular.ttf",
        ]
    )
    for p in candidates:
        if os.path.isfile(p):
            try:
                return ImageFont.truetype(p, size)
            except OSError:
                continue
    return ImageFont.load_default()


def make_og_image() -> None:
    w, h = 1200, 630
    img = Image.new("RGB", (w, h), BG)
    draw = ImageDraw.Draw(img)

    logo = Image.open(LOGO_PATH).convert("RGBA")
    lh = 200
    ratio = lh / logo.height
    lw = int(logo.width * ratio)
    logo = logo.resize((lw, lh), Image.Resampling.LANCZOS)

    x0 = (w - lw) // 2
    y_cursor = 80
    img.paste(logo, (x0, y_cursor), logo)
    y_cursor += lh + 36

    title = "BERENT"
    font_title = load_font(56, bold=True)
    bbox = draw.textbbox((0, 0), title, font=font_title)
    tw = bbox[2] - bbox[0]
    draw.text(((w - tw) // 2, y_cursor), title, fill=COPPER, font=font_title)
    y_cursor += (bbox[3] - bbox[1]) + 28

    tag = "Technik verstehen. Menschen mitnehmen."
    font_tag = load_font(30, bold=False)
    bbox2 = draw.textbbox((0, 0), tag, font=font_tag)
    tw2 = bbox2[2] - bbox2[0]
    draw.text(((w - tw2) // 2, y_cursor), tag, fill=TEXT_MUTED, font=font_tag)

    out = IMAGES / "og-image.png"
    img.save(out, "PNG", optimize=True)
    print(f"Wrote {out}")


def hex_to_rgb(hex_str: str) -> tuple[int, int, int]:
    h = hex_str.lstrip("#")
    return tuple(int(h[i : i + 2], 16) for i in (0, 2, 4))


def make_favicon_dark() -> None:
    """32×32 PNG: Logo auf #090806, gut lesbar in Browser-Tabs."""
    size = 32
    r, g, b = hex_to_rgb(BG)
    logo = Image.open(LOGO_PATH).convert("RGBA")
    pad = 4
    lh = size - 2 * pad
    ratio = lh / logo.height
    lw = int(logo.width * ratio)
    logo = logo.resize((lw, lh), Image.Resampling.LANCZOS)
    x0 = (size - lw) // 2
    y0 = (size - lh) // 2
    img_rgba = Image.new("RGBA", (size, size), (r, g, b, 255))
    img_rgba.paste(logo, (x0, y0), logo)
    out = IMAGES / "favicon-32-dark.png"
    img_rgba.convert("RGB").save(out, "PNG", optimize=True)
    print(f"Wrote {out}")


if __name__ == "__main__":
    if not LOGO_PATH.is_file():
        print(f"Missing logo: {LOGO_PATH}", file=sys.stderr)
        sys.exit(1)
    make_og_image()
    make_favicon_dark()

#!/usr/bin/env python3
"""Generate og-image.png (1200x630) for social media sharing preview.

Uses only Pillow — no native Cairo dependency needed.

Usage:
    python generate-og-image.py

Output:
    assets/og-image.png
"""

from pathlib import Path

from PIL import Image, ImageDraw, ImageFont

# ---------------------------------------------------------------------------
# Config
# ---------------------------------------------------------------------------
WIDTH, HEIGHT = 1200, 630
OUTPUT = Path(__file__).parent / "assets" / "og-image.png"

# Brand colours (from :root CSS variables)
COLOR_CREAM = "#fffbf5"
COLOR_TERRACOTTA = "#c75230"
COLOR_TERRACOTTA_LIGHT = "#f4bdad"
COLOR_TERRACOTTA_BG = "#fdf0ec"
COLOR_GOLD = "#d4a853"
COLOR_TEXT = "#3d2e1f"
COLOR_TEXT_SECONDARY = "#6b5b4d"
COLOR_TEXT_MUTED = "#9c8b7a"
COLOR_LINUX_GRAY = "#888780"

# Dracula terminal colours
TERM_BG = "#282a36"
TERM_TITLEBAR = "#21222c"
TERM_FG = "#f8f8f2"
TERM_GREEN = "#50fa7b"
TERM_PINK = "#ff79c6"
TERM_COMMENT = "#6272a4"
TERM_DOT_RED = "#ff5f57"
TERM_DOT_YELLOW = "#ffbd2e"
TERM_DOT_GREEN = "#28c941"


# ---------------------------------------------------------------------------
# Font helpers — try bundled Inter/JetBrains Mono, fall back to defaults
# ---------------------------------------------------------------------------
FONT_DIR = Path(__file__).parent / "fonts"


def _load_font(
    name_hints: list[str], size: int, bold: bool = False
) -> ImageFont.FreeTypeFont:
    """Try several font paths, fall back to Pillow default."""
    candidates: list[Path] = []
    for hint in name_hints:
        candidates.append(FONT_DIR / hint)
        # Also try common Windows locations
        candidates.append(Path("C:/Windows/Fonts") / hint)

    for p in candidates:
        if p.exists():
            try:
                return ImageFont.truetype(str(p), size)
            except Exception:
                continue

    # Last resort: Pillow's built-in bitmap font (ugly but works)
    try:
        # Try common system sans-serif
        for sys_name in ("arial.ttf", "Arial.ttf", "segoeui.ttf", "DejaVuSans.ttf"):
            try:
                if bold:
                    bold_name = sys_name.replace(".ttf", "bd.ttf").replace(
                        ".TTF", "BD.TTF"
                    )
                    return ImageFont.truetype(bold_name, size)
                return ImageFont.truetype(sys_name, size)
            except Exception:
                continue
    except Exception:
        pass

    return ImageFont.load_default(size=size)


def sans(size: int, bold: bool = False) -> ImageFont.FreeTypeFont:
    hints = (
        ["inter-variable.woff2", "Inter-Bold.ttf", "Inter-Regular.ttf"]
        if not bold
        else ["inter-variable.woff2", "Inter-Bold.ttf"]
    )
    return _load_font(hints, size, bold=bold)


def mono(size: int) -> ImageFont.FreeTypeFont:
    return _load_font(
        ["jetbrains-mono-variable.woff2", "JetBrainsMono-Regular.ttf"], size
    )


# ---------------------------------------------------------------------------
# Drawing helpers
# ---------------------------------------------------------------------------


def rounded_rect(
    draw: ImageDraw.ImageDraw,
    xy: tuple[int, int, int, int],
    radius: int,
    fill: str | None = None,
    outline: str | None = None,
    width: int = 1,
) -> None:
    draw.rounded_rectangle(xy, radius=radius, fill=fill, outline=outline, width=width)


def gradient_bar(
    img: Image.Image, y: int, h: int, left_color: str, right_color: str
) -> None:
    """Draw a horizontal gradient bar."""
    r1, g1, b1 = _hex_to_rgb(left_color)
    r2, g2, b2 = _hex_to_rgb(right_color)
    for x in range(WIDTH):
        t = x / WIDTH
        r = int(r1 + (r2 - r1) * t)
        g = int(g1 + (g2 - g1) * t)
        b = int(b1 + (b2 - b1) * t)
        for dy in range(h):
            img.putpixel((x, y + dy), (r, g, b, 255))


def _hex_to_rgb(hex_color: str) -> tuple[int, int, int]:
    h = hex_color.lstrip("#")
    return int(h[0:2], 16), int(h[2:4], 16), int(h[4:6], 16)


def draw_circle(draw: ImageDraw.ImageDraw, cx: int, cy: int, r: int, fill: str) -> None:
    draw.ellipse([cx - r, cy - r, cx + r, cy + r], fill=fill)


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------


def generate() -> None:
    img = Image.new("RGBA", (WIDTH, HEIGHT), COLOR_CREAM)
    draw = ImageDraw.Draw(img)

    # --- Subtle background circles (decorative) ---
    overlay = Image.new("RGBA", (WIDTH, HEIGHT), (0, 0, 0, 0))
    ov_draw = ImageDraw.Draw(overlay)
    tr, tg, tb = _hex_to_rgb(COLOR_TERRACOTTA)
    ov_draw.ellipse([900, -120, 1300, 280], fill=(tr, tg, tb, 15))
    ov_draw.ellipse([-100, 300, 400, 800], fill=(tr, tg, tb, 12))
    img = Image.alpha_composite(img, overlay)
    draw = ImageDraw.Draw(img)

    # --- Top accent bar (gradient terracotta → gold) ---
    gradient_bar(img, 0, 5, COLOR_TERRACOTTA, COLOR_GOLD)

    # --- Bottom accent bar ---
    gradient_bar(img, HEIGHT - 5, 5, COLOR_TERRACOTTA, COLOR_GOLD)

    # ===================================================================
    # LEFT SIDE — Branding & text
    # ===================================================================
    x_left = 80

    # "QUERENCIA" title
    font_title = sans(56, bold=True)
    draw.text((x_left, 120), "QUERENCIA", fill=COLOR_TERRACOTTA, font=font_title)

    # "LINUX" subtitle
    font_sub = sans(22, bold=True)
    draw.text((x_left + 4, 185), "LINUX", fill=COLOR_LINUX_GRAY, font=font_sub)

    # Tagline
    font_tagline = sans(27)
    draw.text(
        (x_left, 240), "Where Linux Feels at Home", fill=COLOR_TEXT, font=font_tagline
    )

    # Description
    font_desc = sans(16)
    desc_lines = [
        "Atomic, immutable desktop built on AlmaLinux 10",
        "with MATE Desktop. Enterprise-grade stability,",
        "automatic updates, instant rollback.",
    ]
    y_desc = 290
    for line in desc_lines:
        draw.text((x_left, y_desc), line, fill=COLOR_TEXT_SECONDARY, font=font_desc)
        y_desc += 25

    # Feature badges
    badge_font = sans(13, bold=True)
    badges = ["AlmaLinux 10", "MATE Desktop", "Atomic", "AMD GPU"]
    bx = x_left
    by = 395
    badge_h = 34
    badge_pad_x = 20
    badge_gap = 12

    for label in badges:
        bbox = badge_font.getbbox(label)
        tw = bbox[2] - bbox[0]
        bw = tw + badge_pad_x * 2
        rounded_rect(
            draw,
            (bx, by, bx + bw, by + badge_h),
            radius=badge_h // 2,
            fill=COLOR_TERRACOTTA_BG,
            outline=COLOR_TERRACOTTA_LIGHT,
            width=1,
        )
        draw.text(
            (bx + badge_pad_x, by + (badge_h - (bbox[3] - bbox[1])) // 2 - 1),
            label,
            fill=COLOR_TERRACOTTA,
            font=badge_font,
        )
        bx += bw + badge_gap

    # URL
    font_url = mono(14)
    draw.text((x_left, 470), "querencialinux.org", fill=COLOR_TEXT_MUTED, font=font_url)

    # ===================================================================
    # RIGHT SIDE — Terminal mockup
    # ===================================================================
    tx, ty = 640, 140
    tw, th = 480, 340
    term_r = 12

    # Terminal background
    rounded_rect(draw, (tx, ty, tx + tw, ty + th), radius=term_r, fill=TERM_BG)

    # Title bar
    rounded_rect(draw, (tx, ty, tx + tw, ty + 36), radius=term_r, fill=TERM_TITLEBAR)
    # Cover bottom corners of titlebar
    draw.rectangle([tx, ty + 24, tx + tw, ty + 36], fill=TERM_TITLEBAR)

    # Window dots
    dot_y = ty + 18
    draw_circle(draw, tx + 22, dot_y, 6, TERM_DOT_RED)
    draw_circle(draw, tx + 42, dot_y, 6, TERM_DOT_YELLOW)
    draw_circle(draw, tx + 62, dot_y, 6, TERM_DOT_GREEN)

    # Title text
    font_term_title = mono(11)
    title_text = "mate-terminal"
    ttbbox = font_term_title.getbbox(title_text)
    ttw = ttbbox[2] - ttbbox[0]
    draw.text(
        (tx + (tw - ttw) // 2, ty + 10),
        title_text,
        fill=TERM_COMMENT,
        font=font_term_title,
    )

    # Terminal content
    font_term = mono(13)
    cx, cy = tx + 20, ty + 52
    line_h = 24

    term_lines: list[list[tuple[str, str]]] = [
        [(TERM_COMMENT, "# Install from any bootc system")],
        [(TERM_GREEN, "$ "), (TERM_FG, "sudo bootc switch \\")],
        [(TERM_PINK, "  ghcr.io/endegelaende/")],
        [(TERM_PINK, "    querencia-linux:latest")],
        [],
        [(TERM_COMMENT, "Pulling manifest...")],
        [(TERM_GREEN, "✓ "), (TERM_FG, "Queued for next boot.")],
        [(TERM_FG, "  Previous image kept for rollback.")],
        [],
        [(TERM_GREEN, "$ "), (TERM_FG, "sudo reboot")],
    ]

    for parts in term_lines:
        lx = cx
        for color, text in parts:
            draw.text((lx, cy), text, fill=color, font=font_term)
            bbox = font_term.getbbox(text)
            lx += bbox[2] - bbox[0]
        cy += line_h

    # Subtle shadow under terminal
    shadow_color = (*_hex_to_rgb(COLOR_TERRACOTTA), 25)
    for i in range(4):
        ov2 = Image.new("RGBA", (WIDTH, HEIGHT), (0, 0, 0, 0))
        ov2_draw = ImageDraw.Draw(ov2)
        ov2_draw.rounded_rectangle(
            (tx + 4 + i, ty + th + i, tx + tw - 4 - i, ty + th + 6 + i),
            radius=6,
            fill=shadow_color,
        )
        img = Image.alpha_composite(img, ov2)

    # ===================================================================
    # Save
    # ===================================================================
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    final = img.convert("RGB")
    final.save(str(OUTPUT), "PNG", optimize=True)
    size_kb = OUTPUT.stat().st_size / 1024
    print(f"✓ Generated {OUTPUT}  ({WIDTH}×{HEIGHT}, {size_kb:.0f} KB)")


if __name__ == "__main__":
    generate()

#!/usr/bin/env python3
"""Render crisxai5-card.png (1080x1350): an original spotlight card for
@crisxai5 as an AI & crypto expert on X. Drawn with PIL in this session:
dark navy, cyan/violet gradient accents, crisp DejaVu text, no copied logos.
Hook: 'Your feed is 99% noise.' — the card positions @crisxai5 as the 1% signal."""
from PIL import Image, ImageDraw, ImageFont, ImageFilter

W, H = 1080, 1350
FONT = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"
FONTR = "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"

def font(size, bold=True):
    return ImageFont.truetype(FONT if bold else FONTR, size)

img = Image.new("RGB", (W, H), (8, 12, 28))
d = ImageDraw.Draw(img, "RGBA")

# diagonal gradient glow blobs
glow = Image.new("RGBA", (W, H), (0, 0, 0, 0))
gd = ImageDraw.Draw(glow)
gd.ellipse([-220, -180, 520, 420], fill=(34, 211, 238, 70))
gd.ellipse([620, 900, 1320, 1560], fill=(139, 92, 246, 60))
gd.ellipse([760, -120, 1180, 260], fill=(34, 211, 238, 45))
glow = glow.filter(ImageFilter.GaussianBlur(90))
img.paste(Image.alpha_composite(img.convert("RGBA"), glow).convert("RGB"), (0, 0))
d = ImageDraw.Draw(img, "RGBA")

# thin frame
d.rectangle([36, 36, W - 36, H - 36], outline=(34, 211, 238, 160), width=3)

# top pill
pill = "MUST-FOLLOW ON X"
pw = d.textlength(pill, font=font(34)) + 56
d.rounded_rectangle([54, 78, 54 + pw, 78 + 64], radius=32, fill=(34, 211, 238, 255))
d.text((54 + 28, 78 + 13), pill, font=font(34), fill=(8, 12, 28))

# hook
d.text((54, 190), "Your feed is", font=font(78), fill=(255, 255, 255))
d.text((54, 278), "99% noise.", font=font(78), fill=(34, 211, 238))

# handle headline
d.text((54, 420), "@crisxai5", font=font(132), fill=(255, 255, 255))
d.text((54, 560), "AI & CRYPTO EXPERT", font=font(58), fill=(167, 139, 250))
d.text((54, 640), "The 1% signal.", font=font(44, bold=False), fill=(203, 213, 225))

# divider
d.line([54, 730, W - 54, 730], fill=(34, 211, 238, 120), width=3)

# four pillars
pillars = [
    ("AI AGENTS", "Practical takes on agents that actually ship"),
    ("CRYPTO ALPHA", "Sharp reads on the market, no fluff"),
    ("WEB3 TOOLING", "Tools & workflows for builders"),
    ("ON-CHAIN AUTOMATION", "Automate the chain, keep the edge"),
]
y = 780
for title, sub in pillars:
    d.rounded_rectangle([54, y, 118, y + 64], radius=14, fill=(139, 92, 246, 255))
    d.text((86, y + 14), "✓", font=font(34), fill=(255, 255, 255))
    d.text((140, y + 2), title, font=font(40), fill=(255, 255, 255))
    d.text((140, y + 48), sub, font=font(26, bold=False), fill=(148, 163, 184))
    y += 104

# bottom CTA band
d.rounded_rectangle([54, 1210, W - 54, 1210 + 84], radius=18, fill=(34, 211, 238, 255))
cta = "Follow for signal, not noise  →  x.com/crisxai5"
cw = d.textlength(cta, font=font(32))
d.text(((W - cw) / 2, 1210 + 25), cta, font=font(32), fill=(8, 12, 28))

img.save("/home/hatch/workspace/makefun-watch/spotlight-crisxai5/repo/crisxai5-card.png")
print("saved", img.size)

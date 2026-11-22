"""White leaf mark for the header: the green leaf from the Polyglot Asian Medicines icon,
recoloured white on a transparent background (matches the white leaf in the main site's menu)."""
import sys
from PIL import Image

src, dst = sys.argv[1], sys.argv[2]
im = Image.open(src).convert("RGBA")
px = im.load()
out = Image.new("RGBA", im.size, (0, 0, 0, 0))
op = out.load()
for y in range(im.height):
    for x in range(im.width):
        r, g, b, a = px[x, y]
        greenness = g - max(r, b)
        if a > 0 and greenness > 25:
            op[x, y] = (255, 255, 255, min(255, int(a * min(1.0, greenness / 60))))
bbox = out.getbbox()
if bbox:
    out = out.crop(bbox)
out.thumbnail((96, 96), Image.LANCZOS)
out.save(dst, optimize=True)
print("leaf written", out.size)

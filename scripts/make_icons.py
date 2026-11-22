"""Build home-screen icons from the Polyglot icon on kgraph.sg (a ~93x91 PNG)."""
import sys
from PIL import Image

src, out = sys.argv[1], sys.argv[2]
im = Image.open(src).convert("RGBA")
side = max(im.size)
square = Image.new("RGBA", (side, side), (0, 0, 0, 255))
square.paste(im, ((side - im.width) // 2, (side - im.height) // 2), im)

def save(img, size, name):
    img.resize((size, size), Image.LANCZOS).convert("RGB").save(f"{out}/{name}", optimize=True)

save(square, 32, "favicon-32.png")
save(square, 180, "apple-touch-icon.png")
save(square, 192, "icon-192.png")
save(square, 512, "icon-512.png")
# Maskable: artwork kept inside the central safe zone on a black field
mask = Image.new("RGB", (512, 512), (0, 0, 0))
mask.paste(square.resize((400, 400), Image.LANCZOS).convert("RGB"), (56, 56))
mask.save(f"{out}/icon-maskable-512.png", optimize=True)
print("icons written to", out)

"""Build home-screen icons from the Polyglot Asian Medicines leaf icon (polyglotasianmedicine.com)."""
import sys
from PIL import Image

src, out = sys.argv[1], sys.argv[2]
im = Image.open(src).convert("RGBA")
side = max(im.size)
# White field, so transparent corners of the leaf icon read as white on every phone
square = Image.new("RGBA", (side, side), (255, 255, 255, 255))
square.alpha_composite(im, ((side - im.width) // 2, (side - im.height) // 2))

def save(img, size, name):
    img.resize((size, size), Image.LANCZOS).convert("RGB").save(f"{out}/{name}", optimize=True)

save(square, 32, "favicon-32.png")
save(square, 180, "apple-touch-icon.png")
save(square, 192, "icon-192.png")
save(square, 512, "icon-512.png")
# Maskable: artwork kept inside the central safe zone on a white field
mask = Image.new("RGB", (512, 512), (255, 255, 255))
mask.paste(square.resize((400, 400), Image.LANCZOS).convert("RGB"), (56, 56))
mask.save(f"{out}/icon-maskable-512.png", optimize=True)
print("icons written to", out)

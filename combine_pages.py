from PIL import Image
import os

pairs = [(2,3), (4,5), (6,7), (8,9), (10,11), (12,13)]
for a, b in pairs:
    im1 = Image.open(f"/tmp/verify/past_qstns/p-{a:02d}.jpg")
    im2 = Image.open(f"/tmp/verify/past_qstns/p-{b:02d}.jpg")
    h = max(im1.height, im2.height)
    w = im1.width + im2.width
    dst = Image.new('RGB', (w, h), (255, 255, 255))
    dst.paste(im1, (0, 0))
    dst.paste(im2, (im1.width, 0))
    dst.save(f"/tmp/verify/past_qstns/pair_{a}_{b}.jpg", quality=80)

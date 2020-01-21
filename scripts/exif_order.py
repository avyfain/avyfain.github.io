import os
from PIL import Image, ExifTags

# a = {v:k for k, v in ExifTags.TAGS.items()}
# a['DateTimeDigitized']
# > 36868

time_tag = 36868

vals = {}

for f in os.listdir():
    if not f.endswith(('.jpg', '.jpeg')):
        continue
    img = Image.open(f)
    # exif = {
    #     ExifTags.TAGS[k]: v
    #     for k, v in img._getexif().items()
    #     if k in ExifTags.TAGS
    # }
    vals[f] = img.getexif()[36868]

file_order = sorted(vals, key=vals.get)

for idx, f in enumerate(file_order):
    os.rename(f, f'{idx+1}_.jpeg')

for f in os.listdir():
    if f.endswith(('.jpg', '.jpeg')):
        os.rename(f, f.replace('_', ''))

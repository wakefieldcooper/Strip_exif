import exifread
import os
from PIL import Image
import json


def _read_img_and_correct_exif_orientation(path):
    im = Image.open(path)
    tags = {}
    with open(path, 'rb') as f:
        tags = exifread.process_file(f, details=False)
    return tags


directory = input("Please enter directory: ")


for subdir, dirs, files in os.walk(directory):
    for file in files:
        filepath = subdir + os.sep + file
        exif_data = _read_img_and_correct_exif_orientation(filepath)
        print(exif_data)
        # for key, value in exif_data:
        #     print("Key: ", key)
        #     print("value: ", value)
        # # with open("exif_data/{0}.json".format(file.split('.')[0]), "w") as f:
        #     json.dumps(exif_data, f)

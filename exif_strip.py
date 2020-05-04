import os
import sys

import json
from PIL import Image
from PIL.ExifTags import TAGS


def is_image(filepath):
    lfp = filepath.lower()
    return (lfp.endswith('.jpg') or lfp.endswith('.jpeg') or lfp.endswith('.png'))

def strip_file(filepath):
    print('stripping %s... ' % filepath),
    sys.stdout.flush()
    exif_dict = {}
    try:
        img = Image.open(filepath)
        exif_data = img._getexif()
        for (tag, value) in Image.open(filepath)._getexif().items():
            exif_data[TAGS.get(tag)] = value
            print('%s = %s' % (TAGS.get(tag), value))
        # Image.open(filepath).save(filepath)
        print('done')
    except:
        print('error - stopping!')
        sys.exit(-3)

    with open("exif_data/{0}.txt".format(filepath.split("/")[-1].split(".")[0], "w")) as f:
        for line in exif_data:
            str(line)
            f.write(line, "w")
def strip_dir(dirpath):
    if not dirpath.endswith('/'):
        dirpath += '/'
    
    for entry in os.listdir(dirpath):
        filepath = dirpath + entry
        if (not os.path.isfile(filepath)) or (not is_image(filepath)):
            continue
        strip_file(filepath)

if len(sys.argv) < 2:
    print('usage: python %s file1.jpg file2.jpg dir1 dir2 ...' % sys.argv[0])
    sys.exit(-1)

for i in range(1, len(sys.argv)):
    arg = sys.argv[i]
    if os.path.isfile(arg) and is_image(arg):
        strip_file(arg)
    elif os.path.isdir(arg):
        strip_dir(arg)
    else:
        print('invalid input: %s' % arg)
        sys.exit(-2)

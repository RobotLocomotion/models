#!/usr/bin/env python3

from os.path import abspath, basename, dirname, isfile, join, splitext
import tarfile
from urllib.request import urlretrieve

object_names = [
    "003_cracker_box",
    "004_sugar_box",
    "005_tomato_soup_can",
    "006_mustard_bottle",
    "009_gelatin_box",
    "010_potted_meat_can",
]

url_format = "http://ycb-benchmarks.s3-website-us-east-1.amazonaws.com/data/google/{object_name}_google_16k.tgz"
desired_files_format = [
    "{object_name}/google_16k/texture_map.png",
    "{object_name}/google_16k/textured.obj",
    "{object_name}/google_16k/textured.mtl",
]

ycb_dir= dirname(abspath(__file__))
mesh_dir = join(ycb_dir, "meshes")

# Download each object, and reformat path.
for object_name in object_names:
    print(object_name)
    url = url_format.format(object_name=object_name)
    desired_files = [
        x.format(object_name=object_name) for x in desired_files_format]
    tmp_file = join("/tmp/", basename(url))
    if not isfile(tmp_file):
        print(" - Download")
        urlretrieve(url, tmp_file)
    with tarfile.open(tmp_file, mode='r') as tar:
        members = []
        for member in tar.getmembers():
            if member.name in desired_files:
                # Rename.
                _, ext = splitext(member.name)
                member.name = "{}_textured{}".format(object_name, ext)
                print(" - Extract: {}".format(member.name))
                members.append(member)
        tar.extractall(path=mesh_dir, members=members)

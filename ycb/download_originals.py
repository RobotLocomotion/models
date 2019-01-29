#!/usr/bin/env python3

# Copyright 2019 Toyota Research Institute, Inc.
# All rights reserved.
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions are
# met:
#
# Redistributions of source code must retain the above copyright notice,
# this list of conditions and the following disclaimer.  Redistributions
# in binary form must reproduce the above copyright notice, this list of
# conditions and the following disclaimer in the documentation and/or
# other materials provided with the distribution.  Neither the name of
# the Massachusetts Institute of Technology nor the names of its
# contributors may be used to endorse or promote products derived from
# this software without specific prior written permission.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS
# "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT
# LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR
# A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT
# HOLDER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL,
# SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT
# LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE,
# DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY
# THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
# (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
# OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.

"""
Retrieve and rename YCB models. Make minor adjustments.

Flags:
    --modify  Modify files.

Based loosely on the following script:
https://github.com/NVIDIA/Dataset_Utilities/blob/a2f8160/nvdu/tools/nvdu_ycb.py
which can be used in conjunction with DOPE:
https://github.com/NVlabs/Deep_Object_Pose
"""

from os.path import abspath, basename, dirname, isfile, join, splitext
import sys
import tarfile
from urllib.request import urlretrieve

OBJECT_NAMES = [
    "003_cracker_box",
    "004_sugar_box",
    "005_tomato_soup_can",
    "006_mustard_bottle",
    "009_gelatin_box",
    "010_potted_meat_can",
]

# Download 16k version, as that is what DOPE uses.
URL_FORMAT = "http://ycb-benchmarks.s3-website-us-east-1.amazonaws.com/data/google/{object_name}_google_16k.tgz"


def replace_text(filename, old, new):
    with open(filename) as f:
        text = f.read()
    with open(filename, 'w') as f:
        f.write(text.replace(old, new))


def main():
    modify = "--modify" in sys.argv
    if modify:
        print("Downloading AND modifying...")
    else:
        print("Downloading, with NO modification...")

    desired_files_format = [
        "{object_name}/google_16k/texture_map.png",
        "{object_name}/google_16k/textured.obj",
        "{object_name}/google_16k/textured.mtl",
    ]

    ycb_dir= dirname(abspath(__file__))
    mesh_dir = join(ycb_dir, "meshes")

    # Download each object, and reformat path.
    for object_name in OBJECT_NAMES:
        print(object_name)
        url = URL_FORMAT.format(object_name=object_name)
        desired_files = [
            x.format(object_name=object_name) for x in desired_files_format]
        tmp_file = join("/tmp/", basename(url))
        if not isfile(tmp_file):
            print(" - Download")
            urlretrieve(url, tmp_file)
        rename_map = {}  # {old: new}
        with tarfile.open(tmp_file, mode='r') as tar:
            members = []
            for member in tar.getmembers():
                old_name = member.name
                if old_name in desired_files:
                    # Rename.
                    _, ext = splitext(old_name)
                    member.name = "{}_textured{}".format(object_name, ext)
                    rename_map[old_name] = member.name
                    print(" - Extract: {}".format(member.name))
                    members.append(member)
            tar.extractall(path=mesh_dir, members=members)
        assert all([x in rename_map for x in desired_files])
        # Make adjustments to MTL and OBJ files.
        if modify:
            png_file, obj_file, mtl_file = [
                rename_map[x] for x in desired_files]
            mtl_path = join(mesh_dir, mtl_file)
            replace_text(join(mesh_dir, mtl_file), "texture_map.png", png_file)
            replace_text(join(mesh_dir, obj_file), "textured.mtl", mtl_file)


if __name__ == "__main__":
    main()

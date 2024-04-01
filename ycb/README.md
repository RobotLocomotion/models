# YCB Objects

This incorporates a subset of the YCB Models.

## Attribution

All files under `./meshes` attributed to the
[The YCP Object and Model Set](http://ycb-benchmarks.s3-website-us-east-1.amazonaws.com/). Please see
`./meshes/LICENSE.txt` for more information.

The original objects were downloaded on 2019-02-04 via
`./download_originals.py`.

## Modifications

The `.mtl` and `*.obj` files were modified to reflect file renames, then
converted to gltf using `obj2gltf`, then amended to use `*.ktx2` textures.

### OBJ files

The `004_sugar_box_textured` and `006_mustard_bottle` meshes are kept around in
`*.obj` format in addition to `*.gltf` format, in support of obj-specific tests
and tutorials inside Drake; they are not cited by any of the SDFormat files.

## Scope

This contains a small subset of objects from the YCB dataset for use with
Manipulation Station demos in Drake. See
[this discussion](https://github.com/RobotLocomotion/drake/issues/10024#issuecomment-458727931)
for more information about the scope.

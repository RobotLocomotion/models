# Franka meshes

All files under `./meshes` were converted from the original versions
in the Franka ROS package, which is available at:
https://github.com/frankaemika/franka_ros/tree/kinetic-devel/franka_description
SHA d7cd447344.

The license for these files is the Apache 2.0 license.  (see
[`LICENSE`](./LICENSE) for more information).

The `.mtl` and `.obj` files were generated from the `.dae` models in
the original repository.  The models were converted using `pyassimp`.
For example:

```
import pyassimp
pyassimp.export(pyassimp.load("link3.dae"), "link3.obj", file_type="obj")
```

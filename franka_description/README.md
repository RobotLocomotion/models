# Franka

This folder contains a drake-compatible model of the Franka Emika Panda arm.

The model differs from the original ROS model and the real robot. Notably, in
this the "link5split" flavor of the model, link 5 has been split into lower and
upper sections to improve the ability to filter collisions around the wrist. In
all flavors of the hand, the fingers are independently actuated, rather than
using <mimic> tag, which Drake does not yet fully support.

In addition, some tags unsupported by Drake have been removed, to reduce the
burden of warning output. For URDF support details, see:
https://drake.mit.edu/doxygen_cxx/group__multibody__parsing.html

### Rotor Inertia and Gear Ratio

The rotor inertias and gear ratios have been picked so that their combination,
i.e rotor_interia * gear_ratio * gear_ratio, is equal to the reflected interia
provided by Franka for the FR-3 robots.
The reflected inertias for the joints of the Franka FR-3 are:
|Axis data   | reflected inertia (kg m^2)|
|----------- |--------------------------:|
|Axis 1 (A1) |0.605721456                |
|Axis 2 (A2) |0.605721456                |
|Axis 3 (A3) |0.462474144                |
|Axis 4 (A4) |0.462474144                |
|Axis 5 (A5) |0.205544064                |
|Axis 6 (A6) |0.205544064                |
|Axis 7 (A7) |0.205544064                |

### Acceleration Limits

The joint acceleration values are taken based on the older FE-3 Panda (not
the newer FR-3 robot):
https://frankaemika.github.io/docs/control_parameters.html#limits-for-panda

|Axis data   | acceleration limit (rad/s^2)|
|----------- |----------------------------:|
|Axis 1 (A1) |15                           |
|Axis 2 (A2) |7.5                          |
|Axis 3 (A3) |10                           |
|Axis 4 (A4) |12.5                         |
|Axis 5 (A5) |15                           |
|Axis 6 (A6) |20                           |
|Axis 7 (A7) |20                           |

### Collision Filters

#### normal flavor

There is collision filtering applied to ignore collisions between `(panda_link5,
panda_link7)` and between `(panda_link6, panda_link8)`.

#### link5split flavor

The following collision filter groups are defined, all of which filter
collisions within their own group:
- Links 0, 1, 2, and 3 (`group_link0123`)
- Links 1, 2, 3, and 4 (`group_link1234`)
- Links 3, 4, 5 (both lower and upper), and 6 (`group_link3456`)
- Links 5 (lower and upper), 6, and 7 (`group_link567`)
- Link 5 (upper), 6, 7, and 8 (`group_link5upper678`)

For most end-effector designs, you can filter against `group_link5upper678` to
filter impossible EE<->wrist collisions.

### Meshes

The files under `./meshes` are loosely based on the original DAE versions from
the Franka ROS package (as of git sha d7cd447344), available at:
 https://github.com/frankaemika/franka_ros/tree/kinetic-devel/franka_description
but have since been substantially reworked to improve the appearance.

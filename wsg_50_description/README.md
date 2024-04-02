# Schunk WSG50

This folder contains models of the Schunk WSG 50 gripper.

All were created from scratch for use in Drake, and are not based on any other
original SDFormat file from somewhere else.

## Body and stock fingers

For the following meshes:
- `meshes/finger_with_tip`
- `meshes/finger_without_tip`
- `meshes/wsg_body`

The files were created in CAD using Schunk's drawing in the
[product catalog](https://schunk.com/fileadmin/pim/docs/IM0026091.PDF)
(WSG 050-110-P model). Note that these models are not based off
[Schunk's provided CAD model](https://schunk.partcommunity.com/3d-cad-models/wsg-electrical-2-finger-parallel-gripper-universal-gripper-schunk?info=schunk%2Fgreifsysteme_neu%2Fschunk_greifer_neu%2Fparallelgreifer_neu%2Fwsg_asm_at.prj&cwid=7511)
due to
[licensing problems with CADENAS](https://www.cadenas.de/terms-of-use-3d-cad-models).

As this is only based on Schunk's drawing files (not the CAD file), the
dimensions of the model are accurate only up to the published dimensions in the
drawing. Some details such as hole dimensions may not be entirely accurate.

## Punyo bubble fingers

For the following meshes:
- `meshes/bubble_finger`
- `meshes/ellipsoid_bubble_geometry`

The files are based on: https://punyo.tech/#instructions but here are offered
under a different license than that repository.

These are very fine visual meshes that are not intended to be used as collision
models without seeing a considerable slow-down in simulation speed.

Where tutorial resources are created in house, this folder contains the source
files from which the resource can be updated and/or recreated.

The following list should is a mapping of all source files and the resources
they support.

- furnished_office.blend
  - environment_maps
    - env_home_office_full_lights.*
  - models
    - gltf/living_room
    - gltf/curtains
  - Includes the pose information for the furnishing models in
    `furnished_living_room.dmd.yaml`.
- tea_set_01_1k_posed.blend
  - models
    - polyhaven/tea_set_01_1k.gltf/tea_set_01_1k_posed.gltf
- env_color_room.blend
  - environment_maps
    - env_color_room_*.hdr
      - To render a particular map, select the white light, go to its material
        and set the Emissive material's strength property to the desired wattage
        (7.5, 15, or 120 for the current images). The red and blue lights will
        scale accordingly.

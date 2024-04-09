# Skydio 2

This originated from .obj and .mtl files contributed by Abe Bachrach from
Skydio.

Update: 2024-02-24.
- The obj was manually edited to add additional faces to the underside of the
  propellers; previously the propellers were invisible from below.
- The .png file was removed, and the .mtl file was manually edited to replace
  the single color value from the .png directly into the .mtl file.

Update 2024-04-09
 - The .obj/.mtl were converted to .gltf/.bin.
 - Multiple triangles were oriented inconsistently, they been fixed.
 - A single material has been applied to all props (rather than one material
   per prop).
 - The triangles added to the underside of the propellers have been removed
   and the material has been marked as "double sided".

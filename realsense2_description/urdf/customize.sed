# Note that $(...) stuff in the below is NOT special regex characters, we are
# actually matching the xacro text like "$(arg use_mesh)" literally.

s|$(find realsense2_description)/urdf/||;
s|file://$(find realsense2_description)/meshes/|package://drake_models/realsense2_description/meshes/|;
s|$(arg use_mesh)|true|;
s|$(arg use_nominal_extrinsics)|false|;
s|$(arg add_plug)|false|;
s|\.stl|.gltf|;

s|$(find realsense2_description)/urdf/||;
s|file://$(find realsense2_description)/meshes/|../meshes/|;
s|$(arg use_mesh)|true|;
s|$(arg use_nominal_extrinsics)|false|;
s|$(arg add_plug)|false|;
s|package://realsense2_description|package://drake/manipulation/models/realsense2_description|;
s|\.stl|.obj|;

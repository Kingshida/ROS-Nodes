#ID of the point cloud
uint32 id

#Number of points in point cloud
uint32 numPoints

#Descriptor if the point cloud
string descriptor

#Absolute Timestamp of begin of point recording
float64 timestampBegin

#Absolute Timestamp of end of point recording
float64 timestampEnd

#Direction of point acquisition
int8 acquisitionDirection

#Global 3D Vehicle state at begin of point recording
Pose3 globalVs3dBegin

#Global 3D Vehicle state at end of point recording
Pose3 globalVs3dEnd

#Global 3D Vehicle state at begin of point recording, relative
Pose3 localVs3dBegin

#Global 3D Vehicle state at end of point recording, relative
Pose3 localVs3dEnd

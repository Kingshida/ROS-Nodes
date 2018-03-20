Header header

# Current estimation state.
int32 estimationState

# Estimated position and orientation.
geometry_msgs/PoseStamped pose

# Coordinate system information associated with pose.
ezls_msgs/CoordinateSystemInfo csInfo

# Variance vector ( TODO Should be a covariance matrix. ). Stores component-wise variances ( x, y, z ) of the pose.
geometry_msgs/Vector3 variancePosition

# Variance vector ( TODO Should be a covariance matrix. ). Stores component-wise variances ( pitch, roll, yaw ) of the pose.
geometry_msgs/Vector3 varianceOrientation

# Absolute angles vector for all axises [in rad]. 1st comp. = rot. about x-axis. 2nd comp. = rot. about y-axis. 3rd comp. = rot. about z-axis. mptd of vector rotation.
geometry_msgs/Vector3 angles

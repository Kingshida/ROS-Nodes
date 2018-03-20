Header header

# Proposed speed to track an object [m/s].
float64 proposed_speed

# Proposed heading to track an object [-pi,pi].
float64 proposed_heading

# Proposed tilt angle of LMS1
float64 proposed_lms_tilt

# Current robot speed [m/s].
float64 current_speed

# Direction of movement.
uint8 direction

# Tracker status.
uint8 status

# First LMS-Beam to object.
uint32 l_beam

# Last LMS-Beam to object.
uint32 r_beam

# First point of object.
geometry_msgs/Vector3 left

# Calculated middle point of object.
geometry_msgs/Vector3 calculated_middle

# Last point of object.
geometry_msgs/Vector3 right

# Mean point of the object.
geometry_msgs/Vector3 mean

# Security zone parallelogram corner points.
geometry_msgs/Vector3[4] security_zone

# Number of input measurement points.
uint32 num_in_points

# Input measurement points.
geometry_msgs/Vector3[181] in_points

# Current scanline.
string scanline

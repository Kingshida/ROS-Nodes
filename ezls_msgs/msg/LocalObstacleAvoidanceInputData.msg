Header header

# reference yaw [rad] in [-pi, pi]
float64 reference_path_yaw
# reference speed [m/s]
float64 reference_speed

# current (measured) steering-yaw [rad] in [-pi, pi]
float64 current_path_yaw
# robot's current speed [m/s]
float64 current_speed

# The requested direction of travel: 1 == forwards; -1 == backwards
int8 reference_direction

float64 timestamp
int32 command

# Initialization stuff
# --------------------
# Number of particles in the initial particle set
int32 numberOfParticles
# The position to initialize the particle set
geometry_msgs/Point initCoordinate
# Descriptor for the size of the area to use for initialization
float64 initRadius
# Flags if the current dgps position fix is used as the initCoordinate. In this case initCoordinate (see above) is meaningless
bool initAtDgps


# Navigation stuff
# -----------------
# The coordinate of departure for a route-request
geometry_msgs/Point navigationDeparture
# The destination-coordinate for a route-request
geometry_msgs/Point navigationDestination
# Descriptor for the density of the waypoints. The lower the denser
float64 waypointsDelta


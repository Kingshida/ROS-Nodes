Header header

# ID of scanline. Is incremented for each scanner type separately.
uint32 idScanline

# ID of complete scan. Is incremented for each scanner type separately.
uint32 idScan

# ID of scanner. See LmsConfiguration of LmsClient for scanner type enumeration.
int32 idScanner

# Driven distance over ground [in m].
float32 distanceOverGround

# Vector of annotates 3D poses for scanline registration purposes. A vector is used so we can add more poses in the future.
#    Gyroscope-only pose (only gyroscope integration is used): IDX_POSE3_GYRO = 0
#    Filtered pose (fusion of accelerometers, gyroscopes and magnetic compass): IDX_POSE3_FILTER = 1
#    Sensor offset pose (defines how the sensor is positioned and orientated relative to the vehicle coordinate frame): IDX_POSE3_SENSOROFFSET = 2
geometry_msgs/Pose[] poses
    
# Cartesian points. Defined in the CS of the laser scanner sensor.
geometry_msgs/Point32[] points

# Intensity values.
uint32[] intensities


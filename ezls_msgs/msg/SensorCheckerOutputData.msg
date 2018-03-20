Header header



# Estimated accuracy for gps sensor [0...1, 0=worst, 1=best]
float64 accuracyGps

# Position from gps
float64[2] utmGps
    
# Heading from gps
float64 headingGps

# Height from Gps
float64 gpsHeight

# Visible satellites gps
int32 gpsSatellites

# Estimated accuracy for dgps sensor [0...1, 0=worst, 1=best]
float64 accuracyDgps

# Position from dgps
float64[2] utmDgps

# UTM zone from dgps
int32 utmZoneDgps

# Heading from dgps
float64 headingDgps

# Height from dgps
float64 dgpsHeight

# Visible satellites dgps
int32 dgpsSatellites

# Measured value for compass sensor
float64 valueCompass

# Estimated accuracy for tacho sensor [0...1, 0=worst, 1=best]
float64 accuracyTacho

# Measured distance value for tacho
float64 valueTachoDistance

# Measured speed value for tacho
float64 valueTachoSpeed

# Estimated accuracy for left omr sensor [0...1, 0=worst, 1=best]
float64 accuracyOmrLeft

# Measured value for left omr sensor
float64 valueOmrLeft

# Estimated accuracy for right omr sensor [0...1, 0=worst, 1=best]
float64 accuracyOmrRight

# Measured value for right omr sensor
float64 valueOmrRight

# Integrated direction of imu gyro in z-axis
float64 imuDirection

# Raw values from accelerometers
float64[4] valueImuAcc

# Steering angle read from steering node
float64 steeringAngle



# TODO:
# OLD VALUES FROM DOWN HERE, CHECK WHERE NEEDED!!!


# Integrity for compass sensor [0...1, 0=worst, 1=best]
float64 integrityCompass


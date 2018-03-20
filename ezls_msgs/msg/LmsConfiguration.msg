# IP address of laser scanner.
string address

#IP port of laser scanner.
string port

# Type of laser scanner.
uint8 type

# Height over ground of the laser scanner coordinate system [in m].
float64 heightOverGround

# Correctional parameters used in cartesian coordinates transformation. //
# Winkel-Offset zwischen Laserscanner-Koordinatensystem und Welt-Koordinatensystem. Kann mit dem Tool LmsPoseCalibrator ermittelt werden.
float64 pitchOffset

# Winkel zwischen der Horizontalen und der Verbindungslinie der Koordinatensystemsurspruenge [in rad].
# 0.3723 ( entspricht: 21.33 deg / 180 deg * PI )
float64 corrAngle

# Abstand der Koordinatensystemsurspruenge [in m]. Wenn dieser Werte 0 ist wird der Korrekturterm in toCartesian() (mit corrAngle und corrDist) ignoriert.
# 191.10
float64 corrDist



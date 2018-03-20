Header header

# Total number of beams in the scanline (rest of distances array can be ignored).
uint32 numBeams

# Minimal angle bound of opening angle [in radiant].
float64 minAngle

# Maximal angle bound of opening angle [in radiant].
float64 maxAngle

#Angular resolution of the scanline (angle between two beams) [in radiant].
float64 resAngle

# Distance array of the scanline. One distance per beam [in meters].
float64[361] distances

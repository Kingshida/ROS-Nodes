#########################################################################################################################################################
#
# Coordinate system info message.
#
# cs is the coordinate system index
#
#    /**
#     * Undefined coordinate system.
#     */
#    CS_UNDEFINED = -1,
#
#    /**
#     * Geographical coordinate system (World Geodetic System 1984) using latitude and longitude.
#     * Longitude is equivalent to X coordinate.
#     * Latitude is equivalent to Y coordinate.
#     * Altitude is equivalent to Z coordinate.
#     */
#    CS_WGS84 =      1,
#
#    /**
#     * Universal Transverse Mercator coordinate system.
#     * Right is equivalent to X coordinate.
#     * High is equivalent to Y coordinate.
#     * Altitude is equivalent to Z coordinate.
#     */
#    CS_UTM =        2,
#
#    /**
#     * Gauss-Krueger coordinate system.
#     */
#    CS_GK =         3,
#
#    /**
#     * Earth Centred Earth Fixed coordinate system.
#     */
#    CS_ECEF =       4,
#
#
# zone is the zone index. This is used in some coordinate systems like CS_UTM (e.g. "32") in others it can just be ignored.
#
# latitudeBand is the latitude band index. Latitude band characters are encoded as follows: Starting at A=0 the index is incremented with each character.
#
#########################################################################################################################################################

int32 cs
int32 zone
int32 latitudeBand

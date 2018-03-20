# Defines the telegram number of this scanline.
int32 telegrNumber

# Defines the count of complete auto tilt movements.
int32 autoTiltCount

# Defines movement direction of auto tilt movement. True=FromBottomToTop False=FromTopToBottom.
bool autoTiltDirUp

# Zeitstempel der Daten. Die Zeitbasis dieses Zeitstempels ist die des LMS-Serverboards.
uint32 timestamp

# Zeitstempel der Daten [in Sekunden]. Die Zeitbasis dieses Zeitstempels ist die lokalen Systems und wird bei Objekterzeugung gesetzt.
float64 localTimestamp

# Anzahl der aufgenommenen Werte.
uint32 numDistValues

# Entfernungsmaximum dieses Scans [in m].
int32 range

# Startwinkel des Schwenkvorgangs, entspricht erstem Eintrag des Arrays tiltValues[] [in rad].
float64 tiltBegin

# Endwinkel des Schwenkvorgangs, entspricht letztem Eintrag des Arrays tiltValues[] [in rad].
float64 tiltEnd

# Zeigt an, welcher der Interlace Modi verwendet wird.
int32 interlaceMode

# Offset dieser Scanline in Grad * 100 [in deg].
int32 interlaceOffset

# Gibt an, ob der Remissionsmodus aktiv ist (0=aus, 1=an).
int32 remissionMode

# Distanzwerte [in millimeter].
int32[181] distanceValues

# Tiltwerte [in rad].
float64[181] tiltValues

# Remissionswerte.
int32[181] remissionValues

# Zeigt an, ob kartesische Koordinaten fuer diese Scanline vorhanden sind.
bool hasCartesianPoints

# Kartesische Koordinaten dieser Scanline [in meter].
geometry_msgs/Vector3[181] cartesianPoints


# Correctional parameters used in cartesian coordinates transformation. //

# Winkel-Offset zwischen Laserscanner-Koordinatensystem und Welt-Koordinatensystem. Kann mit dem Tool LmsPoseCalibrator ermittelt werden.
float64 pitchOffset

# Winkel zwischen der Horizontalen und der Verbindungslinie der Koordinatensystemsurspruenge [in rad].
# 0.3723 ( entspricht: 21.33 deg / 180 deg * PI )
float64 corrAngle

# Abstand der Koordinatensystemsurspruenge [in m]. Wenn dieser Werte 0 ist wird der Korrekturterm in toCartesian() (mit corrAngle und corrDist) ignoriert.
# 191.10
float64 corrDist


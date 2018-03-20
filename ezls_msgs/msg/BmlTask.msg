# ROS Nachrichtenkopf mit Sequenznummer, Zeitstempel und Frameid 
Header header
# BML Befehl: MOVE, PATROL, DSTRBT(Distribute), GUARD, OBSRV(Observing), RECCE(Reconnaisance), DISENG(Aktuelle Bewegung abbrechen und an der aktuellen Position anhalten), IMINGT ("Imagery intelligence gathering" - Bild anfordern)
string type

# eindeutig identifizierbare Bezeichnung des Befehls
string label 

# Die Variablen xxx_prefix enthalten Schluesselwoerter
# zur Spezifizierung des Ausfuehrungszeitpunktes, welcher entweder in den 
# Variablen xxx_label oder xxx_time festgelegt wird. 
# start_prefix: AT, AFT, STREND (Startet mit dem Ende eines anderen Tasks [start_label]),  
# [(not implement) ASAP, ASAPAF, ASAPNL, AT, BEF, NLT, NOB, STRBEF, STRSTR, STRDUR, STREND, STRAFT]
string start_prefix
# end_prefix: AT, AFT, ENDEND (Ended mit dem Ende eines anderen Tasks [end_label]), 
# [(not implement)ASAP, ASAPAF, ASAPNL, BEF, NLT, NOB, ENDBEF, ENDSTR, ENDDUR, ENDAFT]
string end_prefix

# Das Label des Befehls vor/nach/mit dem dieser Befehl ausgefuehrt werden soll.
# Ist nur gesetzt, wenn STREND bzw. ENDEND gesetzt sind.   
string start_label
string end_label

# Start-/Endzeitpunkt der Ausfuehrung des Befehls.
# Dieser ist immer im Zusammenhang mit xxx_prefix zu betrachten.
# Der Jetzt-Zeitpunkt (sofortige Ausfuehrung) wird durch die 0-Zeit definiert.
time start_time
time end_time

# die Bezeichnung des Befehlgebenden 
string tasker

# der Addresat des Befehls. In diesem Fall wird hier der Name des Roboters stehen. 
string taskee

# Liste von GPS Punkten, die fuer die Ausfuehrung des Befehls notwendig sind.
# x => Latitude, y => Longitude 
geometry_msgs/Point[] points

string TYPE_MOVE   = MOVE
string TYPE_PATROL = PATROL
string TYPE_DSTRBT = DSTRBT
string TYPE_GUARD  = GUARD
string TYPE_OBSRV  = OBSRV
string TYPE_RECCE  = RECCE
string TYPE_DISENG = DISENG
string TYPE_IMINGT = IMINGT

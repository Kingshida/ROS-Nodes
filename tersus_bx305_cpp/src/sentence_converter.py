#!/usr/bin/env python

import re
import time
import calendar

##########################
#  CONVERSION FUNCTIONS  #
##########################

def safe_float(field):
    try:
        return float(field)
    except ValueError:
        return float('NaN')


def safe_int(field):
    try:
        return int(field)
    except ValueError:
        return 0

def convert_latitude(field):
    return safe_float(field[0:2]) + safe_float(field[2:]) / 60.0


def convert_longitude(field):
    return safe_float(field[0:3]) + safe_float(field[3:]) / 60.0

def convert_time(nmea_utc):

    # Get current time in UTC for date information
    utc_struct = time.gmtime()  # immutable, so cannot modify this one
    utc_list = list(utc_struct)
    # If one of the time fields is empty, return NaN seconds
    if not nmea_utc[0:2] or not nmea_utc[2:4] or not nmea_utc[4:6]:
        return float('NaN')
    else:
        hours = int(nmea_utc[0:2])
        minutes = int(nmea_utc[2:4])
        seconds = int(nmea_utc[4:6])
        utc_list[3] = hours
        utc_list[4] = minutes
        utc_list[5] = seconds
        unix_time = calendar.timegm(tuple(utc_list))
        return unix_time



#####################
#  NMEA CONVERSION  #
#####################


# From tersus documentation:
# The general format for a NMEA talker sentence as below.
#
# $ttsss, d1,d2 ...*xx<CR><LF>
#
# Each sentence begins with a '$' and ends with a carriage return/line feed sequence and 
# can be no longer than 80 characters of visible text (plus the line terminators). The data
# fields in a single line are separated by commas. If data for a field is not available, the 
# field  is  omitted,  but  the  delimiting  commas  are  still  there,  with  no  space  
# between them.
#
# EXAMPLES:
#
# $GPGGA,120650.20,5052.16447145,N,00758.68388717,E,1,10,1.7,308.1648,M,48.4796,M,00,0000*6D\r\n"
#
def is_nmea_sentence(sentence):

    # NMEA sentence format:
    # $ttsss,d1,d2,d3,...,dn*xx\r\n
    # TODO:
    # Not quite perfect. Implement a regex for numbers. Right now, something like 15...5 would be ok.
    return re.match(r"  (^\$GP|^\$GN|^\$GL|^\$BD)[A-Z]{3}   # the ttss part \
                        (,[A-Z0-9\.]*)*                     # the ,d1,d2, .. , dn part \
                        (\*[0-9A-Z]{2}\r\n$)                # the *xx<CR><LF> part \
                    ", sentence, re.VERBOSE)

def split_nmea_sentence(nmea_sentence):

    # Remove checksum from sentence
    nmea_sentence = nmea_sentence[0: len(nmea_sentence) - 5]
    fields = [field.strip(',') for field in nmea_sentence.split(',')]
    return fields
    
def get_nmea_sentence_type(nmea_sentence):

    sentence_type = nmea_sentence[3:6] # e.g. GGA, GSV ...
    return sentence_type

# See http://docs.novatel.com/OEM7/Content/Logs/GPGGA.htm
def extract_GGA_data(gga_sentence):
  
    fields = split_nmea_sentence(gga_sentence)
    
    gga = {}
    gga['time'] = convert_time(fields[1])               # UTC time status of position (hours/minutes/seconds/ decimal seconds)
    gga['latitude'] = convert_latitude(fields[2])       # Latitude (DDmm.mm)
    gga['latitude_direction'] = fields[3]               # Latitude direction (N = North, S = South)
    gga['longitude'] =  convert_longitude(fields[4])    # Longitude (DDDmm.mm)
    gga['longitude_direction'] = fields[5]              # Longitude direction (E = East, W = West)
    gga['gps_quality'] = safe_int(fields[6])            # Quality indicator
    gga['num_satellites'] = safe_int(fields[7])         # Number of satellites in use. May be different to the number in view
    gga['hdop'] = safe_float(fields[8])                 # Horizontal dilution of precision
    gga['altitude'] = safe_float(fields[9])             # Antenna altitude above/below mean sea level
    gga['altitude_unit'] = fields[10]                   # Units of antenna altitude (M = metres)
    gga['mean_see_level'] = safe_float(fields[11])      # Undulation - the relationship between the geoid and the WGS84 ellipsoid
    gga['mean_see_level_unit'] = fields[12]             # Units of undulation (M = metres)
    gga['age'] = safe_float(fields[13])                 # Age of correction data (in seconds). Empty, when no differential data is present.
    gga['ref_station_id'] = safe_int(fields[14])        # Differential base station ID. Empty, when no differential data is present.
                                                        
    return gga

# See http://docs.novatel.com/OEM7/Content/Logs/GPRMC.htm
def extract_RMC_data(rmc_sentence):

    fields = split_nmea_sentence(rmc_sentence)

    rmc = {}
    rmc['utc'] = convert_time(fields[1])                # UTC of position (hhmmss)
    rmc['pos_status'] = convert_latitude(fields[2])     # Position status (A = data valid, V = data invalid)
    rmc['latitude'] = fields[3]                         # Latitude (DDmm.mm)
    rmc['latitude_direction'] = fields[4]               # Latitude direction: (N = North, S = South)
    rmc['longitude'] = safe_int(fields[5])              # Longitude (DDDmm.mm)
    rmc['longitude_direction'] = safe_int(fields[6])    # Longitude direction: (E = East, W = West)
    rmc['speed'] = safe_float(fields[7])                # Speed over ground, knots
    rmc['track_true'] = safe_float(fields[8])           # Track made good, degrees True
    rmc['date'] = fields[9]                             # Date: dd/mm/yy
    rmc['magnetic_variation'] = safe_float(fields[10])  # Magnetic variation, degrees
    rmc['magnetic_direction'] = fields[11]              # Magnetic variation direction E/W
    rmc['mode_indicator'] = safe_float(fields[12])      # Positioning system mode indicator
  
    return rmc

def extract_GSV_data(gsv_sentence):

    #"$GPGSV,3,1,11,18,87,050,48,22,56,250,49,21,55,122,49,03,40,284,47*78\r\n"
    #gsv_sentence = "$GPGSV,3,1,11,18,87,050,48,22,56,250,49,21,55,122,49,03,40,284,47*78\r\n"
    fields = split_nmea_sentence(gsv_sentence)

    gsv = {}
    gsv['num_total_msgs'] = safe_int(fields[1])
    gsv['msg_number'] = safe_int(fields[2])
    gsv['num_sat'] = safe_int(fields[3])

    # Extract PRN number, elevation, azimuth and SNR for each satellit.
    # GSV sentence has variable length. Let's find out how many satellits are
    # in this sentence: Take length of array, substract fields we don't
    # care about and divide by 4.
    num_SV = (len(fields) - 4) / 4
    

    # Array with satellit infos
    sat_infos = []    

    for i in range(0, num_SV):
        index = 4 + i*4
        info = {}
        info['prn'] = safe_int(fields[index])
        info['elevation'] = safe_int(fields[index + 1])
        info['azimuth'] = safe_int(fields[index + 2])
        info['SNR'] = safe_int(fields[index + 3])
        
        sat_infos.append(info)

    # Add array to dictionary
    gsv['sat_infos'] = sat_infos

        
    return gsv
    
    
# See http://docs.novatel.com/OEM7/Content/Logs/GPGST.htm#oem7_fw_logs_2909876386_3780968
def extract_GST_data(gst_sentence):

    fields = split_nmea_sentence(gst_sentence)

    gst = {}
    gst['utc'] = convert_time(fields[1])    # UTC time status of position  (hhmmss.ss)
    gst['rms'] = safe_float(fields[2])      # RMS value of the standard deviation of the range inputs to the navigation process 
                                            # Range inputs include pseudoranges and DGPS corrections
    gst['smjr_std'] = safe_float(fields[3]) # Standard deviation of semi-major axis of error ellipse (m)
    gst['smnr_std'] = safe_float(fields[4]) # Standard deviation of semi-minor axis of error ellipse (m)
    gst['orient'] = safe_float(fields[5])   # Orientation of semi-major axis of error ellipse (degrees from true north)
    gst['lat_std'] = safe_float(fields[6])  # Standard deviation of latitude error (m)
    gst['lon_std'] = safe_float(fields[7])  # Standard deviation of longitude error (m)
    gst['alt_std'] = safe_float(fields[8])  # Standard deviation of altitude error (m)
   
    return gst

######################
#  ASCII CONVERSION  #
######################


def is_ascii_sentence(sentence):
         
    return re.match(r"  (^\#[A-Z]+)(,[A-Z0-9\.]*){9};   # Header part \
                        (,[A-Z0-9\._]*)+                # Data part \
                        *[a-z0-9]+\r\n$                 # checksum part \
                    ", sentence, re.VERBOSE)


def get_ascii_sentence_type(sentence):
    # remove the #, then parition the string by ","
    sentence_type = sentence[1:]
    sentence_type = sentence_type.partition(",")
    return sentence_type[0]


# Split the string by "," ";" and "*"
# fields[0] - fields[9] are always  header informations.  
def split_ascii_sentence(sentence):
    return re.split("[;,*]", sentence)


# See http://docs.novatel.com/OEM7/Content/Logs/BESTPOS.htm#oem7_fw_logs_2909876386_8607622
def extract_bestpos_data(sentence):

    pos = {}
            
    fields = split_ascii_sentence(sentence)
    
    if len(fields) is 32:
        pos['sol_stat'] = fields[10]                    # Solution status
        pos['pos_type'] = fields[11]                    # Position type
        pos['lat'] = safe_float(fields[12])             # Latitude (degrees)
        pos['lon'] = safe_float(fields[13])             # Longitude (degrees)
        pos['hgt'] = safe_float(fields[14])             # Height above mean sea level (metres)
        pos['undulation'] = safe_float(fields[15])      # Undulation - the relationship between geoid and ellipsoid (m) of the chosen datum
        pos['datum_id'] = fields[16]                    # Datum ID number 
        pos['lat_std'] = safe_float(fields[17])         # Latitude standard deviation (m)
        pos['lon_std'] = safe_float(fields[18])         # Longitude standard deviation (m)
        pos['hgt_std'] = safe_float(fields[19])         # Height standard deviation (m)
        pos['base_station_id'] = fields[20]             # Base station ID
        pos['diff_age'] = safe_float(fields[21])        # Differential age in seconds
        pos['sol_age'] = safe_float(fields[22])         # Solution age in seconds
        pos['num_SV'] = safe_int(fields[23])            # Number of satellites tracked
        pos['num_sol_SV'] = safe_int(fields[24])        # Number of satellites used in solution
        pos['num_sol_L1_SV'] = safe_int(fields[25])     # Number of satellites with L1/E1/B1 signals used in solution
        pos['num_sol_multi_SV'] = safe_int(fields[26])  # Number of satellites with multi-frequency signals used in solution
        #pos['reserved'] = fields[27]                   # Reserved
        pos['ext_sol_stat'] = fields[28]                # Extended solution status TODO
        pos['GA_BD_sig_mask'] = fields[29]              # Galileo and BeiDou signals used mask TODO
        pos['GPS_GL_sig_mask'] = fields[30]             # GPS and GLONASS signals used mask TODO
    else:
        print("Incomplete BESTPOS sentence received. Will skip sentence")

    return pos

# See http://docs.novatel.com/OEM7/Content/Logs/BESTVEL.htm
def extract_bestvel_data(sentence):

    fields = split_ascii_sentence(sentence)
    
    vel = {}
    vel['sol_stat'] = fields[10]                # Solution status
    vel['vel_type'] = fields[11]                # Velocity type
    vel['latency'] = safe_float(fields[12])     # A measure of the latency in the velocity time tag in seconds. It should be subtracted from the time to give improved results (s)
    vel['age'] = safe_float(fields[13])         # Differential age in seconds
    vel['hor_speed'] = safe_float(fields[14])   # Horizontal speed over ground, in metres per second
    vel['trk gnd'] = safe_float(fields[15])     # Actual direction of motion over ground (track over ground) with respect to True North, in degrees
    vel['vert_speed'] = safe_float(fields[16])  # Vertical speed, in metres per second, where positive values indicate increasing altitude (up) and negative values indicate decreasing altitude (down)
    #vel['reserved'] = safe_float(fields[17])   # Reserved
    
    return vel

# See http://docs.novatel.com/OEM7/Content/Logs/TIME.htm
def extract_time_data(sentence):
    fields = split_ascii_sentence(sentence)

    time = {}
    time['clock_status'] = fields[10]           # Clock model status (not including current measurement data)
    time['offset'] = safe_float(fields[11])     # Receiver clock offset in seconds from GPS reference time.
                                                # A positive offset implies that the receiver clock is ahead of GPS reference time.
                                                # To derive GPS reference time, use the following formula: GPS reference time = receiver time - offset
    time['offset_std'] = safe_float(fields[12]) # Receiver clock offset standard deviation (s)
    time['utc_offset'] = safe_float(fields[13]) # The offset of GPS reference time from UTC time, computed using almanac parameters. 
                                                # UTC time is GPS reference time plus the current UTC offset plus the receiver clock offset:
                                                # UTC time = GPS reference time + offset + UTC offset
    time['utc_year'] = safe_int(fields[14])     # UTC year
    time['utc_month'] = safe_int(fields[15])    # UTC month (0-12). If UTC time is unknown, the value for month is 0.
    time['utc_day'] = safe_int(fields[16])      # UTC day (0-31). If UTC time is unknown, the value for day is 0.
    time['utc_hour'] = safe_int(fields[17])     # UTC hour (0-23)
    time['utc_min'] = safe_int(fields[18])      # UTC minute (0-59)
    time['utc_ms'] = safe_int(fields[19])       # UTC millisecond (0-60999). Maximum of 60999 when leap second is applied.
    time['utc_status'] = safe_int(fields[20])   # UTC status. 0 = Invalid; 1 = Valid; 2 = Warning

    return time

# See http://docs.novatel.com/OEM7/Content/Logs/PSRDOP.htm
def extract_psrdop_data(sentence):
    
    fields = split_ascii_sentence(sentence)

    dop = {}
    dop['gdop'] = safe_float(fields[10])    # Geometric dilution of precision. 
                                            # Assumes 3D position and receiver clock offset (all 4 parameters) are unknown
    dop['pdop'] = safe_float(fields[11])    # Position dilution of precision - assumes 3D position is unknown and receiver clock offset is known
    dop['hdop'] = safe_float(fields[12])    # Horizontal dilution of precision.
    dop['htdop'] = safe_float(fields[13])   # Horizontal position and time dilution of precision.
    dop['tdop'] = safe_float(fields[14])    # Time dilution of precision. 
                                            # Assumes 3D position is known and only the receiver clock offset is unknown.
    dop['cutoff'] = safe_float(fields[15])  # GPS elevation cut-off angle.
    dop['num_PRN'] = safe_int(fields[16])   # Number of satellites PRNs to follow.
    dop['PRN'] = []
    # TODO: test it
    # There are as many PRNs (Pseudo range numbers) as in dop['num_PRN'].
    # Fill them into array
    # PRN of SV PRN tracking, null field until position solution available
    numPRNs = dop['num_PRN']
    for i in range(0, numPRNs):
        dop['PRN'].append( safe_int(fields[17 +i]) ) 
    
    return dop

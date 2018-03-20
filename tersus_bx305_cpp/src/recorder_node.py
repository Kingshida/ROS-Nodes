#!/usr/bin/env python

import time
import rospy
import rospkg
import threading
from bx305_driver import BX305Driver
from ntrip import NTRIPClient

from tersus_bx305.srv import *

sensor = None
wait_for_reset_lock = None
wait_for_FTTF_lock = None
status =  ''

WAIT_TIME = 5 # in seconds
RECORD_TIME = 60 # in seconds
SLEEP_TIME = 0.5 # in seconds

def handle_record(req):

    global sensor
    global wait_for_reset_lock
    global wait_for_FTTF_lock
    global status

    rospack = rospkg.RosPack()
    filepath = rospack.get_path('tersus_bx305') + "/records/" + req.markerName 
   
    print("Start record to:")
    print(filepath)
    
    
    # Reset sensor and wait for complete
    #print("Reset sensor")    
    #reset_start = time.time()
    #sensor.reset()
    #wait_for_reset_lock.acquire()
    #wait_for_reset_lock.wait(30)
    #wait_for_reset_lock.release()
    
    #reset_time = (time.time() - reset_start)
    #print("Needed "+ str(reset_time) + " secs to reset sensor")
    
        
    # Wait for fix
    print("Wait for fix...")
    fix_start = time.time()
    wait_for_FTTF_lock.acquire()
    wait_for_FTTF_lock.wait(360)
    wait_for_FTTF_lock.release()
    FTTF = (time.time() - fix_start) 
    print("FTTF: " + str(FTTF))
    
    # Record
    time.sleep(WAIT_TIME)
    sensor.enable_file_log(filepath,str(FTTF))

    record_start = time.time()
    record_duration = 0.0
    while record_duration < RECORD_TIME :
 
        sys.stdout.write("\rStatus: " + str(status) + " --- " + str(RECORD_TIME - record_duration) + " s       ")
        sys.stdout.flush()
        time.sleep(SLEEP_TIME)
        record_duration = time.time() - record_start
    
    print("Done recording")

    sensor.disable_file_log()
    

    return True
    

def reset_cb():
    global wait_for_reset_lock

    wait_for_reset_lock.acquire()
    wait_for_reset_lock.notify()
    wait_for_reset_lock.release()

def BESTPOS_cb(sentence):

    global wait_for_FTTF_lock

    global status    
    status = sentence['sol_stat']

    print(status)

    if(status == "SOL_COMPUTED"):
        wait_for_FTTF_lock.acquire()
        wait_for_FTTF_lock.notify()
        wait_for_FTTF_lock.release()

        
def gps_recorder():

    global sensor

    global wait_for_FTTF_lock
    global wait_for_reset_lock

    rospy.init_node('bx305_recorder_node', anonymous=True)
    rate = rospy.Rate(50) # 50z
    rec_service = rospy.Service('/record', startMessure , handle_record) 

    port = rospy.get_param('~port', '/dev/ttyUSB0')
    baud = rospy.get_param('~baud', 115200)
    sensor = BX305Driver(port, baud)
    
    connected = sensor.connect()
    if(not connected):
       rospy.logerr("Could not open serial connection. Will exit")
       return

    rospy.loginfo("Connection established.")


    sensor.unlogall()

    # Configure outputs...    
    # COM1
    sensor.log_ontime("gpgga", 1)  
    sensor.log_ontime("gpgsv", 1)
    sensor.log_ontime("gprmc", 1)

    sensor.log_ontime("bestposa", 1)
    #sensor.log_ontime("bestposb", 1)
    sensor.log_ontime("psrvela", 1)
    sensor.log_ontime("timea", 1)   
    sensor.log_onchanged("psrdopa") 
    #sensor.log_ontime("psrdopa",1)
    sensor.log_ontime("rangeb", 1)   

    #COM2
    sensor.log_ontime("gpgga", 1, "COM2")
    #sensor.log_ontime("gpgsv", 1, "COM2")

    sensor.set_reset_done_callback(reset_cb)
    sensor.set_BESTPOS_callback(BESTPOS_cb)
    sensor.saveconfig()


    """
    ntrip = NTRIPClient("195.227.70.116", 2101, "VRS_3_2G_NW_h", "nf-unisieezls1", "klamue", "/dev/ttyUSB1", 115200)
    ntrip.connect()
    """
    rospy.loginfo("BX305 recorder node started sucessfully...")

    wait_for_reset_lock = threading.Condition()
    wait_for_FTTF_lock = threading.Condition()

    while not rospy.is_shutdown():    
        rate.sleep()


    sensor.disconnect()

if __name__ == '__main__':
    try:
        gps_recorder()
    except rospy.ROSInterruptException:
        print("exit")            
        

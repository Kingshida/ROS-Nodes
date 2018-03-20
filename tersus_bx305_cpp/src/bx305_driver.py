#!/usr/bin/env python

import threading
import sentence_converter as parser

from serial_interface import SerialInterface
from byte_parser import ByteParser
from byte_parser import ReadState


# TODO: integrate support for checksum 
class BX305Driver():

    def __init__(self, server_com_port, baudrate):
        
        # Setup serial interface.
        self._serial_interface = SerialInterface(server_com_port, baudrate, 50)
        self._serial_interface.set_read_callback(self._on_serial_read)

        # The byte parser analyses the byte string from the sensor
        # and divides it into individual sentences.
        self._byte_parser = ByteParser()

        self._current_sentence = bytearray()

        # If set, all raw data from serial port will be stored to this file.
        self._log_file = None 

        # Locks
        #self._ack_lock = threading.Condition()	
        self._wait_for_sentence_lock = threading.Condition()
        self._wait_for_sentence_type = None
        self._wait_for_sentence_data = None

        # Callbacks for NMEA sentences.
        self._GGA_cb = None
        self._RMC_cb = None
        self._GSV_cb = None
        self._GST_cb = None

        # Callbacks for ASCII sentences.
        self._BESTPOS_cb = None
        self._BESTVEL_cb = None
        self._TIME_cb = None
        self._PSRDOP_cb = None

        # Special callbacks.
        self._reset_cb = None
        
        # GSV information is sometimes split up into multiple sentences.
        # Need to gather all informations before calling callback.
        self._GSV_data = None

        # Total number of sentences until the GSV data we are currently
        # waiting for is complete
        self._received_GSV_sentences = 0

        
        
    def __del__(self):
        self._driver.stop()

    # Open connection to sensor. If success, start gathering data.
    def connect(self):

        if(self._serial_interface.open_connection()):
            self._serial_interface.start()
            return True
        else:
            return False

    def disconnect(self):
        self._serial_interface.stop()
        self._serial_interface.close_connection()


    # Unlog all
    def unlogall(self):
        command = "unlogall\r\n"
        self._serial_interface.write_safe(command)

    # Reset/ Restart sensor
    def reset(self):
        command = "reset\r\n"
        self._serial_interface.write_safe(command)

    def saveconfig(self):
        command = "saveconfig\r\n"
        self._serial_interface.write_safe(command)

    # Repeatedly log
    def log_ontime(self, log_type, ontime, sensor_com = ""):
        
        # Clamp ontime 
        ontime = max(0.05, min(ontime, 20))
        command = "log " + sensor_com + " " + log_type + " ontime " + str(ontime) + "\r\n"
        self._serial_interface.write_safe(command)
    
        # TODO: wait for ACK
        #self._ack_lock.acquire()
        #self._ack_lock.wait(2)
        #self._ack_lock.release()
        


    # Log a single sentence once. Will wait for result 
    def log_once(self, log_type, sensor_com = "" ):
        # Remember what we are waiting for, then clear old data
        #self._wait_for_sentence_type = log_type
        #self._wait_for_sentence_data = None

        # Send request
        command = "log " + sensor_com + " " + log_type + " once\r\n"
        self._serial_interface.write_safe(command)

        # Wait until result is available or 3 seconds have passed
        #self._wait_for_sentence_lock.acquire()
        #self._wait_for_sentence_lock.wait(3)
        #self._wait_for_sentence_lock.release()

        #return self._wait_for_sentence_data
        
    # Log whenever this sentence changed
    def log_onchanged(self, log_type , sensor_com = ""):

        command = "log " + sensor_com + " " + log_type + " onchanged\r\n"
        self._serial_interface.write_safe(command)
    

    # Callback setters for NMEA sentences
    def set_GGA_callback(self, GGA_callback):
        self._GGA_cb = GGA_callback

    def set_RMC_callback(self, RMC_callback):
        self._RMC_cb = RMC_callback

    def set_GSV_callback(self, GSV_callback):
        self._GSV_cb = GSV_callback

    def set_GST_callback(self, GST_callback):
        self._GST_cb = GST_callback


    # Callback setters for ASCII sentences
    def set_BESTPOS_callback(self, BESTPOS_callback):
        self._BESTPOS_cb = BESTPOS_callback

    def set_BESTVEL_callback(self, BESTVEL_callback):
        self._BESTVEL_cb = BESTVEL_callback

    def set_TIME_callback(self, TIME_callback):
        self._TIME_cb = TIME_callback

    def set_PSRDOP_callback(self, PSRDOP_callback):
        self._PSRDOP_cb = PSRDOP_callback


    # Callback setters for special callbacks
    def set_reset_done_callback(self, reset_done_callback):
        self._reset_cb = reset_done_callback


    def _restart_byte_parser(self):
        
        self._byte_parser.restart()
        self._current_sentence = bytearray()

    def _on_serial_read(self, data):

        for b in data:
            #print(chr(b))
            # Update state machine
            self._byte_parser.update_state(b)
            self._current_sentence.append(b)

            
            if(self._byte_parser.parsing_done()):

                if (self._byte_parser.get_state() == ReadState.SUCCESS_BINARY):
                    self._on_new_binary_data(self._current_sentence)
                    self._restart_byte_parser()

                elif (self._byte_parser.get_state() == ReadState.SUCCESS_ASCII):
                    self._on_new_ascii_data(self._current_sentence)
                    self._restart_byte_parser()
                        
                elif (self._byte_parser.get_state() == ReadState.SUCCESS_ACK):
                    self._on_ack()
                    self._restart_byte_parser()

                elif (self._byte_parser.get_state() == ReadState.ERROR):
                    #print("ERROR parsing")
                    #print(chr(b))
                    self._restart_byte_parser()
    
                elif (self._byte_parser.get_state() == ReadState.SUCCESS_RESET):
                    self._on_reset()
                    self._restart_byte_parser()
                    

        
        # Save to log file, if enabled
        if(self._log_file is not None):
            self._log_file.write(data)
        

    def _on_new_ascii_data(self, data):


        if(parser.is_nmea_sentence(data)):
            self._handle_nmea_sentence(data)

        elif(parser.is_ascii_sentence(data)):
            self._handle_ascii_sentence(data)


    def _handle_nmea_sentence(self, sentence):
        nmea_type = parser.get_nmea_sentence_type(sentence)

        if(nmea_type == "GGA" and self._GGA_cb is not None):
            self._GGA_cb(parser.extract_GGA_data(sentence))

        if(nmea_type == "RMC" and self._RMC_cb is not None):
            self._RMC_cb(parser.extract_RMC_data(sentence))

        if(nmea_type == "GST" and self._GST_cb is not None):
            self._GST_cb(parser.extract_GST_data(sentence))

        # GSV is a special case: Data is split up in multiple sentences. Need to wait until all 
        # data is available, before calling callback function.
        if(nmea_type == "GSV" and self._GSV_cb is not None):
            data = parser.extract_GSV_data(sentence)
            
            
            total_msg = data.pop('num_total_msgs')
            this_msg = data.pop('msg_number')
        
            if(self._GSV_data is None): 

                # Data consists of only one sentence. Call callback directly.
                if  (total_msg == this_msg): 

                    self._GSV_cb(data)
                # Multiple sentences. Save this data to complete it later.
                else:
                    self._GSV_data = data

            else:
                self._GSV_data['sat_infos'].extend(data['sat_infos'])
                if  (total_msg == this_msg):
                    self._GSV_cb(self._GSV_data)
                    self._GSV_data = None
                

    def _handle_ascii_sentence(self, sentence):
        ascii_type = parser.get_ascii_sentence_type(sentence)

        if(ascii_type == "BESTPOSA" and self._BESTPOS_cb is not None):
            result = parser.extract_bestpos_data(sentence)
            if(result):
                self._BESTPOS_cb(result)

        if(ascii_type == "BESTVELA" and self._BESTVEL_cb is not None):
            self._BESTVEL_cb(parser.extract_bestvel_data(sentence))

        if(ascii_type == "TIMEA" and self._TIME_cb is not None):
            self._TIME_cb(parser.extract_time_data(sentence))

        if(ascii_type == "PSRDOPA" and self._PSRDOP_cb is not None):
            self._PSRDOP_cb(parser.extract_psrdop_data(sentence))

    def _on_new_binary_data(self, data):

        if(self._binaryFile is not None):
            self._binaryFile.write(data)




    def _on_ack(self):

        #print("ACK arrived")
        #self._ack_lock.acquire()
        #self._ack_lock.notify()
        #self._ack_lock.release()
        pass

    def _on_reset(self):

        print("RESET received")
        if(self._reset_cb is not None):
            self._reset_cb()
        
    # Log to file
    def enable_file_log(self, filepath):

        try:
            self._log_file = open(filepath, 'w')
        except IOError as e:
            self._log_file = None
            print("Error opening record file.")
    
    # Disable log to file
    def disable_file_log(self):
    
        if(self._log_file is not None):
            self._log_file.close()

        self._log_file = None


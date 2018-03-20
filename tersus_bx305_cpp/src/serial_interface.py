#!/usr/bin/env python

import serial
import threading
import time
from sys import version_info

# TODO TIMEOUT
class SerialInterface(threading.Thread):

    
    # Init method
    def __init__(self, port, baudrate, frequency=100):
        
        # Threading
        threading.Thread.__init__(self)         
        self._thread = None

        # Serial
        self._ser = serial.Serial()
        self._ser.baudrate = baudrate
        self._ser.port = port

        # Will be called when new data has read from serial port
        self._data_callback = None     

        # Calculate sleep time in seconds
        if frequency < 0:    
              frequency = 1.0
        self._sleep_time = 1.0 / frequency


        # The serial API has changed slightly between python2 and python3
        self._use_python3 = True
        if version_info < (3, 0, 0):
            self._use_python3 = False
            
    
    # Delete method
    def __del__(self):
        self.closeConnection()

    # Set the function that will be called when a new sentence has arrived
    def set_read_callback(self, callback):
        self._data_callback = callback

    # Open serial connection. Returns true, if serial port
    # is open.
    def open_connection(self):

        try:

            self._ser.open()
            return self._is_serial_open()
                
        except serial.SerialException as err:
            print("Failed to open serial port: ", str(err)) 
            return False
 
    # Write a command to the serial port. Returns true if command was written.
    def write_safe(self, message):

        if(self._is_serial_open()):
            try: 
                self._ser.write(message)
                return True
            except SerialTimeoutException:
                print("Failed to write to serial port - Timeout")                
                return False



    # Stop the working thread
    def stop(self):
        self._keepRunning = False
        self._thread.join()

    # Close the serial connection
    def close_connection(self):
        self._ser.close()


    # Start gathering data from sensor in a new thread
    def start(self):
        self._reset_serial_input_buffer()

        self._keepRunning = True                
        self._thread = threading.Thread(target=self.run_read_loop, args=())
        self._thread.daemon = True
        self._thread.start()

    # Read all bytes from the serial buffer continuously
    def run_read_loop(self):
        
        while self._keepRunning and self._is_serial_open:
    
            num_bytes = self._get_input_buffer_size()

            if(num_bytes > 0):
                try:
                    raw_read = self._ser.read(num_bytes)       
                except serial.SerialException as err:
                    print("Reading from serial port did fail: " )
                    print(str(err))
                    raw_read = ''
    
                if len(raw_read) > 0 and self._data_callback is not None:
                    self._data_callback(bytearray(raw_read))

            time.sleep(self._sleep_time)
            print(self._sleep_time)



    # Returns True if serial port is open, false otherwise.    
    # Indepent from python version
    def _is_serial_open(self):
        if self._use_python3:
            return self._ser.is_open
        else:
            return self._ser.isOpen()
                        
    # Reset the serial input buffer.    
    # Indepent from python version
    def _reset_serial_input_buffer(self):
        if self._use_python3:
            self._ser.reset_input_buffer()
        else:
            self._ser.flushInput()

    # Get the number of bytes that are waiting in the input buffer.
    # Indepent from python version
    # TODO: buffer overflow check
    def _get_input_buffer_size(self):
        if self._use_python3:
            return self._ser.in_waiting
        else:
            return self._ser.inWaiting()

    """
    # Start gathering data from sensor in a new thread
    def start(self):
        self._ser.reset_input_buffer()

        self._keepRunning = True                
        self._thread = threading.Thread(target=self.run, args=())
        self._thread.daemon = True
        self._thread.start() 

    def run(self):
      
        while self._keepRunning and self._ser.is_open:
            
            try:
                sentence = self._ser.readline()
            except SerialException as err:
                print("Reading from serial port did fail: " + err.what())
                sentence = ''
            
            self._data_callback(sentence)
    """
    

 


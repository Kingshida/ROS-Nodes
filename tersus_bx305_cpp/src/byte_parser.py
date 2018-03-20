#!/usr/bin/env python

#from enum import IntEnum
from struct import unpack

class ReadState():
    START = 1           # START state

    SYNC1 = 2           # sync byte 1 received
    SYNC2 = 3           # sync byte 2 received
    SYNC3 = 4           # sync byte 3 received
    READ_HEADER = 5     # read until header is complete
    READ_MESSAGE = 6    # read until message is complete
    SUCCESS_BINARY = 7  # END state - parsing of binary data was successful

    READ_ASCII_MSG = 8  # read until \r\n was received
    READ_LINEFEED = 9   # wait for linefeed
    SUCCESS_ASCII = 10  # END state - parsing ascii success

    ACK1 = 11           # ACK byte 1 recveived
    ACK2 = 12           # ACK byte 2 recveived
    SUCCESS_ACK = 13    # END state - ACK reveiced

    ERROR = 14          # END state - something went wrong

    RESET1 = 15         # reset byte 1 received
    RESET2 = 16         # reset byte 2 received
    RESET3 = 17         # reset byte 3 received
    RESET4 = 18         # reset byte 4 received
    RESET5 = 19         # reset byte 5 received
    SUCCESS_RESET = 20  # END state - reset complete
    
    
# TODO: Class description
# Implements a finite state machine
class ByteParser():

    def __init__(self):
        
        # Current state of the state machine
        self._state = ReadState.START
    
        # The header. Need to store it to get message length
        self._header_buffer = bytearray()
        
        # Length of the header. Should be 28, but always check
        self._header_len = 0

        # Length of the message that is currently read
        self._msg_len = 0
    
        # How many bytes of message already read
        self._num_msg_bytes_read = 0

    def __del__(self):
        pass

    # Restart state engine
    def restart(self):
        self._state = ReadState.START 
        self._header_buffer = bytearray()
        self._header_len = 0
        self._msg_len = 0
        self._num_msg_bytes_read = 0

    # Returns the current state of the state machine
    def get_state(self):
        return self._state

    # Returns true, if state machine has reached an end state. 
    # Returns false otherwise (parsing still in progress)
    def parsing_done(self):
        return self._state == ReadState.ERROR or self._state == ReadState.SUCCESS_BINARY or self._state == ReadState.SUCCESS_ASCII or self._state == ReadState.SUCCESS_ACK or self._state == ReadState.SUCCESS_RESET
        

    # TODO: with dictionaries?
    def update_state(self, sign):

            sign = chr(sign)
            if self._state is ReadState.START:
               self._start_state_transitions(sign)

            # ASCII states
            elif self._state is ReadState.READ_ASCII_MSG:
                self._read_ascii_state_transitions(sign)

            elif self._state is ReadState.READ_LINEFEED:
                self._read_linefeed_state_transitions(sign)
        
            # BINARY states
            elif self._state is ReadState.SYNC1:
               self._sync1_state_transitions(sign)

            elif self._state is ReadState.SYNC2:
               self._sync2_state_transitions(sign)

            elif self._state is ReadState.SYNC3:
               self._sync3_state_transitions(sign)

            elif self._state is ReadState.READ_HEADER:
               self._read_header_state_transitions(sign)

            elif self._state is ReadState.READ_MESSAGE:
               self._read_message_state_transitions(sign)

            # Acknowledgment
            elif self._state is ReadState.ACK1:
                self._ack1_state_transitions(sign)

            elif self._state is ReadState.ACK2:
                self._ack2_state_transitions(sign)


            # Reset
            elif self._state is ReadState.RESET1:
                self._reset1_state_transitions(sign)

            elif self._state is ReadState.RESET2:
                self._reset2_state_transitions(sign)

            elif self._state is ReadState.RESET3:
                self._reset3_state_transitions(sign)

            elif self._state is ReadState.RESET4:
                self._reset4_state_transitions(sign)

            elif self._state is ReadState.RESET5:
                self._reset5_state_transitions(sign)



    def _start_state_transitions(self, sign):

        # Start of a binary message.
        if sign == '\xaa':
            self._state = ReadState.SYNC1
 
        # Start of an ASCII message.
        elif sign == '\x24' or sign == '\x23': # '$' or '#'
            self._state = ReadState.READ_ASCII_MSG    

        # Start of acknowledgment
        elif sign == '\x3C': # <
            self._state = ReadState.ACK1

        # Start of Reset 
        elif sign == '\x5B': # [
            self._state = ReadState.RESET1

        # These are often input acknowledgments: "input: log com1 ..."
        # We can ignore them
        else: 
            self._state = ReadState.ERROR

    def _read_ascii_state_transitions(self, sign):

        if sign == '\x0d':
            self._state = ReadState.READ_LINEFEED
    

    def _read_linefeed_state_transitions(self, sign):
        
        if sign == '\x0a':
            self._state = ReadState.SUCCESS_ASCII
        else:
            self._state = ReadState.ERROR


    def _sync1_state_transitions(self, sign):
    
        if sign == '\x44':
            self._state = ReadState.SYNC2
        else:
            self._state = ReadState.ERROR



    def _sync2_state_transitions(self, sign):

        if sign == '\x12':
            self._state = ReadState.SYNC3
        else:
            self._state = ReadState.ERROR



    def _sync3_state_transitions(self, sign):
        
        # Header length includes the 3 sync bytes.
        # We already read them, so subtract 3
        self._header_len = 28 - 3 # TODO: read from message
        self._num_header_bytes_read = 0
        
        self._header_buffer.append(sign)

        self._state = ReadState.READ_HEADER



    def _read_header_state_transitions(self, sign):
        
        self._header_buffer.append(sign)  

        if len(self._header_buffer) == self._header_len:

            # Message length (in bytes) does not include CRC, thus add 4
            self._msg_len = self._header_buffer[5] + 256 * self._header_buffer[6] + 4  
            
            self._num_msg_bytes_read = 0
            self._state = ReadState.READ_MESSAGE            

    def _read_message_state_transitions(self, sign):
        
        self._num_msg_bytes_read += 1

        if self._num_msg_bytes_read == self._msg_len:
            self._state = ReadState.SUCCESS_BINARY

    def _ack1_state_transitions(self, sign):
        if sign == '\x4F': # O
            self._state = ReadState.ACK2
        else:
            self._state = ReadState.ERROR

    def _ack2_state_transitions(self, sign):

        if sign == '\x4B': # K
            self._state = ReadState.SUCCESS_ACK
        else:
            self._state = ReadState.ERROR

    def _reset1_state_transitions(self, sign):

        if sign == '\x43': # C
            self._state = ReadState.RESET2
        else:
            self._state = ReadState.ERROR

    def _reset2_state_transitions(self, sign):

        if sign == '\x4F': # O
            self._state = ReadState.RESET3
        else:
            self._state = ReadState.ERROR

    def _reset3_state_transitions(self, sign):

        if sign == '\x4D': # M
            self._state = ReadState.RESET4
        else:
            self._state = ReadState.ERROR

    def _reset4_state_transitions(self, sign):

        if sign == '\x31' or sign == '\x32' or sign == '\x33' : # 1, 2 or 3
            self._state = ReadState.RESET5
        else:
            self._state = ReadState.ERROR

    def _reset5_state_transitions(self, sign):

        if sign == '\x5D': # ]
            self._state = ReadState.SUCCESS_RESET
        else:
            self._state = ReadState.ERROR


"""autogenerated by genpy from ezls_msgs/VsalOpticalMovementRecognitionRightCommandRequest.msg. Do not edit."""
import sys
python3 = True if sys.hexversion > 0x03000000 else False
import genpy
import struct


class VsalOpticalMovementRecognitionRightCommandRequest(genpy.Message):
  _md5sum = "bc5858f4465f8a4c5606f8f3c4897127"
  _type = "ezls_msgs/VsalOpticalMovementRecognitionRightCommandRequest"
  _has_header = False #flag to mark the presence of a Header object
  _full_text = """




int32 command

uint8 state
uint8 framerate
uint8 shutter
uint8 address
uint8 data



"""
  __slots__ = ['command','state','framerate','shutter','address','data']
  _slot_types = ['int32','uint8','uint8','uint8','uint8','uint8']

  def __init__(self, *args, **kwds):
    """
    Constructor. Any message fields that are implicitly/explicitly
    set to None will be assigned a default value. The recommend
    use is keyword arguments as this is more robust to future message
    changes.  You cannot mix in-order arguments and keyword arguments.

    The available fields are:
       command,state,framerate,shutter,address,data

    :param args: complete set of field values, in .msg order
    :param kwds: use keyword arguments corresponding to message field names
    to set specific fields.
    """
    if args or kwds:
      super(VsalOpticalMovementRecognitionRightCommandRequest, self).__init__(*args, **kwds)
      #message fields cannot be None, assign default values for those that are
      if self.command is None:
        self.command = 0
      if self.state is None:
        self.state = 0
      if self.framerate is None:
        self.framerate = 0
      if self.shutter is None:
        self.shutter = 0
      if self.address is None:
        self.address = 0
      if self.data is None:
        self.data = 0
    else:
      self.command = 0
      self.state = 0
      self.framerate = 0
      self.shutter = 0
      self.address = 0
      self.data = 0

  def _get_types(self):
    """
    internal API method
    """
    return self._slot_types

  def serialize(self, buff):
    """
    serialize message into buffer
    :param buff: buffer, ``StringIO``
    """
    try:
      _x = self
      buff.write(_struct_i5B.pack(_x.command, _x.state, _x.framerate, _x.shutter, _x.address, _x.data))
    except struct.error as se: self._check_types(se)
    except TypeError as te: self._check_types(te)

  def deserialize(self, str):
    """
    unpack serialized message in str into this message instance
    :param str: byte array of serialized message, ``str``
    """
    try:
      end = 0
      _x = self
      start = end
      end += 9
      (_x.command, _x.state, _x.framerate, _x.shutter, _x.address, _x.data,) = _struct_i5B.unpack(str[start:end])
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e) #most likely buffer underfill


  def serialize_numpy(self, buff, numpy):
    """
    serialize message with numpy array types into buffer
    :param buff: buffer, ``StringIO``
    :param numpy: numpy python module
    """
    try:
      _x = self
      buff.write(_struct_i5B.pack(_x.command, _x.state, _x.framerate, _x.shutter, _x.address, _x.data))
    except struct.error as se: self._check_types(se)
    except TypeError as te: self._check_types(te)

  def deserialize_numpy(self, str, numpy):
    """
    unpack serialized message in str into this message instance using numpy for array types
    :param str: byte array of serialized message, ``str``
    :param numpy: numpy python module
    """
    try:
      end = 0
      _x = self
      start = end
      end += 9
      (_x.command, _x.state, _x.framerate, _x.shutter, _x.address, _x.data,) = _struct_i5B.unpack(str[start:end])
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e) #most likely buffer underfill

_struct_I = genpy.struct_I
_struct_i5B = struct.Struct("<i5B")
"""autogenerated by genpy from ezls_msgs/VsalOpticalMovementRecognitionRightCommandResponse.msg. Do not edit."""
import sys
python3 = True if sys.hexversion > 0x03000000 else False
import genpy
import struct


class VsalOpticalMovementRecognitionRightCommandResponse(genpy.Message):
  _md5sum = "358e233cde0c8a8bcfea4ce193f8fc15"
  _type = "ezls_msgs/VsalOpticalMovementRecognitionRightCommandResponse"
  _has_header = False #flag to mark the presence of a Header object
  _full_text = """

bool success


"""
  __slots__ = ['success']
  _slot_types = ['bool']

  def __init__(self, *args, **kwds):
    """
    Constructor. Any message fields that are implicitly/explicitly
    set to None will be assigned a default value. The recommend
    use is keyword arguments as this is more robust to future message
    changes.  You cannot mix in-order arguments and keyword arguments.

    The available fields are:
       success

    :param args: complete set of field values, in .msg order
    :param kwds: use keyword arguments corresponding to message field names
    to set specific fields.
    """
    if args or kwds:
      super(VsalOpticalMovementRecognitionRightCommandResponse, self).__init__(*args, **kwds)
      #message fields cannot be None, assign default values for those that are
      if self.success is None:
        self.success = False
    else:
      self.success = False

  def _get_types(self):
    """
    internal API method
    """
    return self._slot_types

  def serialize(self, buff):
    """
    serialize message into buffer
    :param buff: buffer, ``StringIO``
    """
    try:
      buff.write(_struct_B.pack(self.success))
    except struct.error as se: self._check_types(se)
    except TypeError as te: self._check_types(te)

  def deserialize(self, str):
    """
    unpack serialized message in str into this message instance
    :param str: byte array of serialized message, ``str``
    """
    try:
      end = 0
      start = end
      end += 1
      (self.success,) = _struct_B.unpack(str[start:end])
      self.success = bool(self.success)
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e) #most likely buffer underfill


  def serialize_numpy(self, buff, numpy):
    """
    serialize message with numpy array types into buffer
    :param buff: buffer, ``StringIO``
    :param numpy: numpy python module
    """
    try:
      buff.write(_struct_B.pack(self.success))
    except struct.error as se: self._check_types(se)
    except TypeError as te: self._check_types(te)

  def deserialize_numpy(self, str, numpy):
    """
    unpack serialized message in str into this message instance using numpy for array types
    :param str: byte array of serialized message, ``str``
    :param numpy: numpy python module
    """
    try:
      end = 0
      start = end
      end += 1
      (self.success,) = _struct_B.unpack(str[start:end])
      self.success = bool(self.success)
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e) #most likely buffer underfill

_struct_I = genpy.struct_I
_struct_B = struct.Struct("<B")
class VsalOpticalMovementRecognitionRightCommand(object):
  _type          = 'ezls_msgs/VsalOpticalMovementRecognitionRightCommand'
  _md5sum = '15a13b1b0c0518aaba0a14d7b0149e3d'
  _request_class  = VsalOpticalMovementRecognitionRightCommandRequest
  _response_class = VsalOpticalMovementRecognitionRightCommandResponse
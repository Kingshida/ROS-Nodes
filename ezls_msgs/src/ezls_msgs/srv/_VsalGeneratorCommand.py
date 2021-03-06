"""autogenerated by genpy from ezls_msgs/VsalGeneratorCommandRequest.msg. Do not edit."""
import sys
python3 = True if sys.hexversion > 0x03000000 else False
import genpy
import struct


class VsalGeneratorCommandRequest(genpy.Message):
  _md5sum = "cbdaf7d28a137e2c7fdf946b2bad2eb0"
  _type = "ezls_msgs/VsalGeneratorCommandRequest"
  _has_header = False #flag to mark the presence of a Header object
  _full_text = """




int32 command

uint8 state
uint16 agitatorMinRPM
uint8 loadInc
uint8 loadDec


"""
  __slots__ = ['command','state','agitatorMinRPM','loadInc','loadDec']
  _slot_types = ['int32','uint8','uint16','uint8','uint8']

  def __init__(self, *args, **kwds):
    """
    Constructor. Any message fields that are implicitly/explicitly
    set to None will be assigned a default value. The recommend
    use is keyword arguments as this is more robust to future message
    changes.  You cannot mix in-order arguments and keyword arguments.

    The available fields are:
       command,state,agitatorMinRPM,loadInc,loadDec

    :param args: complete set of field values, in .msg order
    :param kwds: use keyword arguments corresponding to message field names
    to set specific fields.
    """
    if args or kwds:
      super(VsalGeneratorCommandRequest, self).__init__(*args, **kwds)
      #message fields cannot be None, assign default values for those that are
      if self.command is None:
        self.command = 0
      if self.state is None:
        self.state = 0
      if self.agitatorMinRPM is None:
        self.agitatorMinRPM = 0
      if self.loadInc is None:
        self.loadInc = 0
      if self.loadDec is None:
        self.loadDec = 0
    else:
      self.command = 0
      self.state = 0
      self.agitatorMinRPM = 0
      self.loadInc = 0
      self.loadDec = 0

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
      buff.write(_struct_iBH2B.pack(_x.command, _x.state, _x.agitatorMinRPM, _x.loadInc, _x.loadDec))
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
      (_x.command, _x.state, _x.agitatorMinRPM, _x.loadInc, _x.loadDec,) = _struct_iBH2B.unpack(str[start:end])
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
      buff.write(_struct_iBH2B.pack(_x.command, _x.state, _x.agitatorMinRPM, _x.loadInc, _x.loadDec))
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
      (_x.command, _x.state, _x.agitatorMinRPM, _x.loadInc, _x.loadDec,) = _struct_iBH2B.unpack(str[start:end])
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e) #most likely buffer underfill

_struct_I = genpy.struct_I
_struct_iBH2B = struct.Struct("<iBH2B")
"""autogenerated by genpy from ezls_msgs/VsalGeneratorCommandResponse.msg. Do not edit."""
import sys
python3 = True if sys.hexversion > 0x03000000 else False
import genpy
import struct


class VsalGeneratorCommandResponse(genpy.Message):
  _md5sum = "358e233cde0c8a8bcfea4ce193f8fc15"
  _type = "ezls_msgs/VsalGeneratorCommandResponse"
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
      super(VsalGeneratorCommandResponse, self).__init__(*args, **kwds)
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
class VsalGeneratorCommand(object):
  _type          = 'ezls_msgs/VsalGeneratorCommand'
  _md5sum = '8ecc2e0c1b7442bac261be021efa9f92'
  _request_class  = VsalGeneratorCommandRequest
  _response_class = VsalGeneratorCommandResponse

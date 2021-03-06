"""autogenerated by genpy from ezls_msgs/ReflexesCommand.msg. Do not edit."""
import sys
python3 = True if sys.hexversion > 0x03000000 else False
import genpy
import struct


class ReflexesCommand(genpy.Message):
  _md5sum = "08ebc9297f7c2e91e14953d79344a032"
  _type = "ezls_msgs/ReflexesCommand"
  _has_header = False #flag to mark the presence of a Header object
  _full_text = """float64 timestamp
int32 command

float64 referenceSpeed
float64 referenceHeading

int8 referenceDirection

"""
  __slots__ = ['timestamp','command','referenceSpeed','referenceHeading','referenceDirection']
  _slot_types = ['float64','int32','float64','float64','int8']

  def __init__(self, *args, **kwds):
    """
    Constructor. Any message fields that are implicitly/explicitly
    set to None will be assigned a default value. The recommend
    use is keyword arguments as this is more robust to future message
    changes.  You cannot mix in-order arguments and keyword arguments.

    The available fields are:
       timestamp,command,referenceSpeed,referenceHeading,referenceDirection

    :param args: complete set of field values, in .msg order
    :param kwds: use keyword arguments corresponding to message field names
    to set specific fields.
    """
    if args or kwds:
      super(ReflexesCommand, self).__init__(*args, **kwds)
      #message fields cannot be None, assign default values for those that are
      if self.timestamp is None:
        self.timestamp = 0.
      if self.command is None:
        self.command = 0
      if self.referenceSpeed is None:
        self.referenceSpeed = 0.
      if self.referenceHeading is None:
        self.referenceHeading = 0.
      if self.referenceDirection is None:
        self.referenceDirection = 0
    else:
      self.timestamp = 0.
      self.command = 0
      self.referenceSpeed = 0.
      self.referenceHeading = 0.
      self.referenceDirection = 0

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
      buff.write(_struct_di2db.pack(_x.timestamp, _x.command, _x.referenceSpeed, _x.referenceHeading, _x.referenceDirection))
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
      end += 29
      (_x.timestamp, _x.command, _x.referenceSpeed, _x.referenceHeading, _x.referenceDirection,) = _struct_di2db.unpack(str[start:end])
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
      buff.write(_struct_di2db.pack(_x.timestamp, _x.command, _x.referenceSpeed, _x.referenceHeading, _x.referenceDirection))
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
      end += 29
      (_x.timestamp, _x.command, _x.referenceSpeed, _x.referenceHeading, _x.referenceDirection,) = _struct_di2db.unpack(str[start:end])
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e) #most likely buffer underfill

_struct_I = genpy.struct_I
_struct_di2db = struct.Struct("<di2db")

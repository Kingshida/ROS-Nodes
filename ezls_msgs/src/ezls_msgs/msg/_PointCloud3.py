"""autogenerated by genpy from ezls_msgs/PointCloud3.msg. Do not edit."""
import sys
python3 = True if sys.hexversion > 0x03000000 else False
import genpy
import struct

import geometry_msgs.msg
import ezls_msgs.msg

class PointCloud3(genpy.Message):
  _md5sum = "2085127750292f93d439d4179b8df902"
  _type = "ezls_msgs/PointCloud3"
  _has_header = False #flag to mark the presence of a Header object
  _full_text = """# Parameters
PointCloud3Parameters params

#Vector of Points of Point Cloud
geometry_msgs/Point[] points

#Valid bits
uint8[] valid

================================================================================
MSG: ezls_msgs/PointCloud3Parameters
#ID of the point cloud
uint32 id

#Number of points in point cloud
uint32 numPoints

#Descriptor if the point cloud
string descriptor

#Absolute Timestamp of begin of point recording
float64 timestampBegin

#Absolute Timestamp of end of point recording
float64 timestampEnd

#Direction of point acquisition
int8 acquisitionDirection

#Global 3D Vehicle state at begin of point recording
Pose3 globalVs3dBegin

#Global 3D Vehicle state at end of point recording
Pose3 globalVs3dEnd

#Global 3D Vehicle state at begin of point recording, relative
Pose3 localVs3dBegin

#Global 3D Vehicle state at end of point recording, relative
Pose3 localVs3dEnd

================================================================================
MSG: ezls_msgs/Pose3
geometry_msgs/Vector3 position
geometry_msgs/Vector3 orientation

================================================================================
MSG: geometry_msgs/Vector3
# This represents a vector in free space. 

float64 x
float64 y
float64 z
================================================================================
MSG: geometry_msgs/Point
# This contains the position of a point in free space
float64 x
float64 y
float64 z

"""
  __slots__ = ['params','points','valid']
  _slot_types = ['ezls_msgs/PointCloud3Parameters','geometry_msgs/Point[]','uint8[]']

  def __init__(self, *args, **kwds):
    """
    Constructor. Any message fields that are implicitly/explicitly
    set to None will be assigned a default value. The recommend
    use is keyword arguments as this is more robust to future message
    changes.  You cannot mix in-order arguments and keyword arguments.

    The available fields are:
       params,points,valid

    :param args: complete set of field values, in .msg order
    :param kwds: use keyword arguments corresponding to message field names
    to set specific fields.
    """
    if args or kwds:
      super(PointCloud3, self).__init__(*args, **kwds)
      #message fields cannot be None, assign default values for those that are
      if self.params is None:
        self.params = ezls_msgs.msg.PointCloud3Parameters()
      if self.points is None:
        self.points = []
      if self.valid is None:
        self.valid = ''
    else:
      self.params = ezls_msgs.msg.PointCloud3Parameters()
      self.points = []
      self.valid = ''

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
      buff.write(_struct_2I.pack(_x.params.id, _x.params.numPoints))
      _x = self.params.descriptor
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      buff.write(struct.pack('<I%ss'%length, length, _x))
      _x = self
      buff.write(_struct_2db24d.pack(_x.params.timestampBegin, _x.params.timestampEnd, _x.params.acquisitionDirection, _x.params.globalVs3dBegin.position.x, _x.params.globalVs3dBegin.position.y, _x.params.globalVs3dBegin.position.z, _x.params.globalVs3dBegin.orientation.x, _x.params.globalVs3dBegin.orientation.y, _x.params.globalVs3dBegin.orientation.z, _x.params.globalVs3dEnd.position.x, _x.params.globalVs3dEnd.position.y, _x.params.globalVs3dEnd.position.z, _x.params.globalVs3dEnd.orientation.x, _x.params.globalVs3dEnd.orientation.y, _x.params.globalVs3dEnd.orientation.z, _x.params.localVs3dBegin.position.x, _x.params.localVs3dBegin.position.y, _x.params.localVs3dBegin.position.z, _x.params.localVs3dBegin.orientation.x, _x.params.localVs3dBegin.orientation.y, _x.params.localVs3dBegin.orientation.z, _x.params.localVs3dEnd.position.x, _x.params.localVs3dEnd.position.y, _x.params.localVs3dEnd.position.z, _x.params.localVs3dEnd.orientation.x, _x.params.localVs3dEnd.orientation.y, _x.params.localVs3dEnd.orientation.z))
      length = len(self.points)
      buff.write(_struct_I.pack(length))
      for val1 in self.points:
        _x = val1
        buff.write(_struct_3d.pack(_x.x, _x.y, _x.z))
      _x = self.valid
      length = len(_x)
      # - if encoded as a list instead, serialize as bytes instead of string
      if type(_x) in [list, tuple]:
        buff.write(struct.pack('<I%sB'%length, length, *_x))
      else:
        buff.write(struct.pack('<I%ss'%length, length, _x))
    except struct.error as se: self._check_types(se)
    except TypeError as te: self._check_types(te)

  def deserialize(self, str):
    """
    unpack serialized message in str into this message instance
    :param str: byte array of serialized message, ``str``
    """
    try:
      if self.params is None:
        self.params = ezls_msgs.msg.PointCloud3Parameters()
      if self.points is None:
        self.points = None
      end = 0
      _x = self
      start = end
      end += 8
      (_x.params.id, _x.params.numPoints,) = _struct_2I.unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.params.descriptor = str[start:end].decode('utf-8')
      else:
        self.params.descriptor = str[start:end]
      _x = self
      start = end
      end += 209
      (_x.params.timestampBegin, _x.params.timestampEnd, _x.params.acquisitionDirection, _x.params.globalVs3dBegin.position.x, _x.params.globalVs3dBegin.position.y, _x.params.globalVs3dBegin.position.z, _x.params.globalVs3dBegin.orientation.x, _x.params.globalVs3dBegin.orientation.y, _x.params.globalVs3dBegin.orientation.z, _x.params.globalVs3dEnd.position.x, _x.params.globalVs3dEnd.position.y, _x.params.globalVs3dEnd.position.z, _x.params.globalVs3dEnd.orientation.x, _x.params.globalVs3dEnd.orientation.y, _x.params.globalVs3dEnd.orientation.z, _x.params.localVs3dBegin.position.x, _x.params.localVs3dBegin.position.y, _x.params.localVs3dBegin.position.z, _x.params.localVs3dBegin.orientation.x, _x.params.localVs3dBegin.orientation.y, _x.params.localVs3dBegin.orientation.z, _x.params.localVs3dEnd.position.x, _x.params.localVs3dEnd.position.y, _x.params.localVs3dEnd.position.z, _x.params.localVs3dEnd.orientation.x, _x.params.localVs3dEnd.orientation.y, _x.params.localVs3dEnd.orientation.z,) = _struct_2db24d.unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      self.points = []
      for i in range(0, length):
        val1 = geometry_msgs.msg.Point()
        _x = val1
        start = end
        end += 24
        (_x.x, _x.y, _x.z,) = _struct_3d.unpack(str[start:end])
        self.points.append(val1)
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.valid = str[start:end].decode('utf-8')
      else:
        self.valid = str[start:end]
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
      buff.write(_struct_2I.pack(_x.params.id, _x.params.numPoints))
      _x = self.params.descriptor
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      buff.write(struct.pack('<I%ss'%length, length, _x))
      _x = self
      buff.write(_struct_2db24d.pack(_x.params.timestampBegin, _x.params.timestampEnd, _x.params.acquisitionDirection, _x.params.globalVs3dBegin.position.x, _x.params.globalVs3dBegin.position.y, _x.params.globalVs3dBegin.position.z, _x.params.globalVs3dBegin.orientation.x, _x.params.globalVs3dBegin.orientation.y, _x.params.globalVs3dBegin.orientation.z, _x.params.globalVs3dEnd.position.x, _x.params.globalVs3dEnd.position.y, _x.params.globalVs3dEnd.position.z, _x.params.globalVs3dEnd.orientation.x, _x.params.globalVs3dEnd.orientation.y, _x.params.globalVs3dEnd.orientation.z, _x.params.localVs3dBegin.position.x, _x.params.localVs3dBegin.position.y, _x.params.localVs3dBegin.position.z, _x.params.localVs3dBegin.orientation.x, _x.params.localVs3dBegin.orientation.y, _x.params.localVs3dBegin.orientation.z, _x.params.localVs3dEnd.position.x, _x.params.localVs3dEnd.position.y, _x.params.localVs3dEnd.position.z, _x.params.localVs3dEnd.orientation.x, _x.params.localVs3dEnd.orientation.y, _x.params.localVs3dEnd.orientation.z))
      length = len(self.points)
      buff.write(_struct_I.pack(length))
      for val1 in self.points:
        _x = val1
        buff.write(_struct_3d.pack(_x.x, _x.y, _x.z))
      _x = self.valid
      length = len(_x)
      # - if encoded as a list instead, serialize as bytes instead of string
      if type(_x) in [list, tuple]:
        buff.write(struct.pack('<I%sB'%length, length, *_x))
      else:
        buff.write(struct.pack('<I%ss'%length, length, _x))
    except struct.error as se: self._check_types(se)
    except TypeError as te: self._check_types(te)

  def deserialize_numpy(self, str, numpy):
    """
    unpack serialized message in str into this message instance using numpy for array types
    :param str: byte array of serialized message, ``str``
    :param numpy: numpy python module
    """
    try:
      if self.params is None:
        self.params = ezls_msgs.msg.PointCloud3Parameters()
      if self.points is None:
        self.points = None
      end = 0
      _x = self
      start = end
      end += 8
      (_x.params.id, _x.params.numPoints,) = _struct_2I.unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.params.descriptor = str[start:end].decode('utf-8')
      else:
        self.params.descriptor = str[start:end]
      _x = self
      start = end
      end += 209
      (_x.params.timestampBegin, _x.params.timestampEnd, _x.params.acquisitionDirection, _x.params.globalVs3dBegin.position.x, _x.params.globalVs3dBegin.position.y, _x.params.globalVs3dBegin.position.z, _x.params.globalVs3dBegin.orientation.x, _x.params.globalVs3dBegin.orientation.y, _x.params.globalVs3dBegin.orientation.z, _x.params.globalVs3dEnd.position.x, _x.params.globalVs3dEnd.position.y, _x.params.globalVs3dEnd.position.z, _x.params.globalVs3dEnd.orientation.x, _x.params.globalVs3dEnd.orientation.y, _x.params.globalVs3dEnd.orientation.z, _x.params.localVs3dBegin.position.x, _x.params.localVs3dBegin.position.y, _x.params.localVs3dBegin.position.z, _x.params.localVs3dBegin.orientation.x, _x.params.localVs3dBegin.orientation.y, _x.params.localVs3dBegin.orientation.z, _x.params.localVs3dEnd.position.x, _x.params.localVs3dEnd.position.y, _x.params.localVs3dEnd.position.z, _x.params.localVs3dEnd.orientation.x, _x.params.localVs3dEnd.orientation.y, _x.params.localVs3dEnd.orientation.z,) = _struct_2db24d.unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      self.points = []
      for i in range(0, length):
        val1 = geometry_msgs.msg.Point()
        _x = val1
        start = end
        end += 24
        (_x.x, _x.y, _x.z,) = _struct_3d.unpack(str[start:end])
        self.points.append(val1)
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.valid = str[start:end].decode('utf-8')
      else:
        self.valid = str[start:end]
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e) #most likely buffer underfill

_struct_I = genpy.struct_I
_struct_2db24d = struct.Struct("<2db24d")
_struct_2I = struct.Struct("<2I")
_struct_3d = struct.Struct("<3d")

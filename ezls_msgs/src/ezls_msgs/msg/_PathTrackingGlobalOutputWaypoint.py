"""autogenerated by genpy from ezls_msgs/PathTrackingGlobalOutputWaypoint.msg. Do not edit."""
import sys
python3 = True if sys.hexversion > 0x03000000 else False
import genpy
import struct

import geometry_msgs.msg
import ezls_msgs.msg

class PathTrackingGlobalOutputWaypoint(genpy.Message):
  _md5sum = "b5bc25cce791cfdd35b5578209c48c67"
  _type = "ezls_msgs/PathTrackingGlobalOutputWaypoint"
  _has_header = False #flag to mark the presence of a Header object
  _full_text = """GlobalWaypoint3 waypoint

================================================================================
MSG: ezls_msgs/GlobalWaypoint3
# Pose3 of waypoint
ezls_msgs/Pose3 pose

# ID of waypoint
int32 id

# Type of waypoint
uint32 type

# Is waypoint reached
bool reached

# Distance to be reached
float64 reachingDistance

#Event number
int32 event


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
"""
  __slots__ = ['waypoint']
  _slot_types = ['ezls_msgs/GlobalWaypoint3']

  def __init__(self, *args, **kwds):
    """
    Constructor. Any message fields that are implicitly/explicitly
    set to None will be assigned a default value. The recommend
    use is keyword arguments as this is more robust to future message
    changes.  You cannot mix in-order arguments and keyword arguments.

    The available fields are:
       waypoint

    :param args: complete set of field values, in .msg order
    :param kwds: use keyword arguments corresponding to message field names
    to set specific fields.
    """
    if args or kwds:
      super(PathTrackingGlobalOutputWaypoint, self).__init__(*args, **kwds)
      #message fields cannot be None, assign default values for those that are
      if self.waypoint is None:
        self.waypoint = ezls_msgs.msg.GlobalWaypoint3()
    else:
      self.waypoint = ezls_msgs.msg.GlobalWaypoint3()

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
      buff.write(_struct_6diIBdi.pack(_x.waypoint.pose.position.x, _x.waypoint.pose.position.y, _x.waypoint.pose.position.z, _x.waypoint.pose.orientation.x, _x.waypoint.pose.orientation.y, _x.waypoint.pose.orientation.z, _x.waypoint.id, _x.waypoint.type, _x.waypoint.reached, _x.waypoint.reachingDistance, _x.waypoint.event))
    except struct.error as se: self._check_types(se)
    except TypeError as te: self._check_types(te)

  def deserialize(self, str):
    """
    unpack serialized message in str into this message instance
    :param str: byte array of serialized message, ``str``
    """
    try:
      if self.waypoint is None:
        self.waypoint = ezls_msgs.msg.GlobalWaypoint3()
      end = 0
      _x = self
      start = end
      end += 69
      (_x.waypoint.pose.position.x, _x.waypoint.pose.position.y, _x.waypoint.pose.position.z, _x.waypoint.pose.orientation.x, _x.waypoint.pose.orientation.y, _x.waypoint.pose.orientation.z, _x.waypoint.id, _x.waypoint.type, _x.waypoint.reached, _x.waypoint.reachingDistance, _x.waypoint.event,) = _struct_6diIBdi.unpack(str[start:end])
      self.waypoint.reached = bool(self.waypoint.reached)
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
      buff.write(_struct_6diIBdi.pack(_x.waypoint.pose.position.x, _x.waypoint.pose.position.y, _x.waypoint.pose.position.z, _x.waypoint.pose.orientation.x, _x.waypoint.pose.orientation.y, _x.waypoint.pose.orientation.z, _x.waypoint.id, _x.waypoint.type, _x.waypoint.reached, _x.waypoint.reachingDistance, _x.waypoint.event))
    except struct.error as se: self._check_types(se)
    except TypeError as te: self._check_types(te)

  def deserialize_numpy(self, str, numpy):
    """
    unpack serialized message in str into this message instance using numpy for array types
    :param str: byte array of serialized message, ``str``
    :param numpy: numpy python module
    """
    try:
      if self.waypoint is None:
        self.waypoint = ezls_msgs.msg.GlobalWaypoint3()
      end = 0
      _x = self
      start = end
      end += 69
      (_x.waypoint.pose.position.x, _x.waypoint.pose.position.y, _x.waypoint.pose.position.z, _x.waypoint.pose.orientation.x, _x.waypoint.pose.orientation.y, _x.waypoint.pose.orientation.z, _x.waypoint.id, _x.waypoint.type, _x.waypoint.reached, _x.waypoint.reachingDistance, _x.waypoint.event,) = _struct_6diIBdi.unpack(str[start:end])
      self.waypoint.reached = bool(self.waypoint.reached)
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e) #most likely buffer underfill

_struct_I = genpy.struct_I
_struct_6diIBdi = struct.Struct("<6diIBdi")
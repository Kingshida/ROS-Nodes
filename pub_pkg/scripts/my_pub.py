#!/usr/bin/env python
import rospy
from pub_pkg.msg import my_data

def talker():
    pub = rospy.Publisher('chatter', my_data, queue_size=10)      # 'chatter' -> topic name, as a handler for subscribers
    rospy.init_node('talker', anonymous=True)
    rate = rospy.Rate(10) # 10hz
    msg = my_data()
    msg.Name = "Vamshi"
    msg.age = 24
    while not rospy.is_shutdown():
        #hello_str = "%s %s" % (msg, rospy.get_time())
        rospy.loginfo(msg)
        pub.publish(msg)
        rate.sleep()

if __name__ == "__main__":
    try:
        talker()
    except rospy.ROSInterruptException:
        pass

#!/usr/bin/env python
# Above statement -> To make sure the current script is executed as a python script

# Publishes velocity data to turtlesim node
# rosrun turtlesim turtlesim_node

import rospy
from geometry_msgs.msg import Twist                 # Importing custom message defined in same package


def move_node():
    pub_h = rospy.Publisher("turtle1/cmd_vel", Twist, queue_size = 10)
    # pub_h -> Handle for the publisher node
    # "turtle1/cmd_vel" -> topic name (to communicate with turtlesim node)
    # Twist -> type of message we are publishing

    rospy.init_node("move_node", anonymous=True)    # Initialising the node

    rate = rospy.Rate(1)                            # Rate in Hz

    vel = Twist()
    vel.linear.x= 0.1
    vel.angular.z = -0.1

    while not rospy.is_shutdown():
        rospy.loginfo(vel)                          # Prints data on screen, updates logfile, writes to rosout
        pub_h.publish(vel)                          # Publishes data to given topic
        rate.sleep()                                # sleeps to maintain desired rate


if __name__ == "__main__":
    try:
        move_node()
    except rospy.ROSInterruptException:
        pass
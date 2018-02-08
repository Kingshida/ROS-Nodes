#!/usr/bin/env python
# Above statement -> To make sure the current script is executed as a python script

import rospy
from depend_pkg.msg import additional_data   # Importing custom message defined in same package
from pub_pkg.msg import my_data              # Importing custom message defined in different package


def pub_details():
    pub_h = rospy.Publisher("pub", additional_data, queue_size = 10)
    rospy.init_node("pub_details", anonymous=True)
    rate = rospy.Rate(1)

    person = my_data()
    curr_city = additional_data()

    person.Name = "Vamshi"
    person.age = 24
    curr_city = "Siegen"

    while not rospy.is_shutdown():
        out = "%s is %s years old and lives in %s " %(person.Name, person.age, curr_city)
        rospy.loginfo(out)
        pub_h.publish(out)
        rate.sleep()


if __name__ == "__main__":
    try:
        pub_details()
    except rospy.ROSInterruptException:
        pass
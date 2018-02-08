#!/usr/bin/env python
# Above statement -> To make sure the current script is executed as a python script

# Subscribes message published to "turtle1/cmd_vel" topic and saves to .xls file

import xlwt                                         # For writing spreadshet

import rospy
from geometry_msgs.msg import Twist

# Spreadsheet initialisation
name = ['x', 'y', 'z']
style0 = xlwt.easyxf('font: name Times New Roman, bold on', num_format_str='#,##0.00')
styl_heading = xlwt.easyxf('font: name Times New Roman, color-index red, bold on; pattern: pattern solid, fore_color yellow; align: wrap on, horiz centre, vert centre; borders:top thick, bottom thick, left thick, right thick;')

wb = xlwt.Workbook()
ws = wb.add_sheet('Velocity')

ws.write_merge(0, 0, 1, 6, 'Twist', styl_heading)
ws.write_merge(1, 1, 1, 3, 'Linear', styl_heading)
ws.write_merge(1, 1, 4, 6, 'Angular', styl_heading)
ws.write(2, 0, 'Time stamp', styl_heading)
for i in range(len(name)):
    ws.write(2, i+1, name[i], styl_heading)
    ws.write(2, i+4, name[i], styl_heading)

row = 3


# Writing data to spreadsheet
def save_data(s_data):
    global row
    save_d = [rospy.get_time(), s_data.linear.x, s_data.linear.y, s_data.linear.z, s_data.angular.x, s_data.angular.y, s_data.angular.z]
    for j in range(len(save_d)):
        ws.write(row, j, save_d[j], style0)
    row += 1


def callback(data):
    rospy.loginfo(rospy.get_caller_id() + " I heard: \n %s", data)
    save_data(data)


def listen_vel():
    rospy.init_node('listen_vel', anonymous=True)           # Initialising the node
    rospy.Subscriber('turtle1/cmd_vel', Twist, callback)
    rospy.spin()
    wb.save('Velocity_Data.xls')                            # Saves in home folder after exit


if __name__ == "__main__":
    try:
        listen_vel()
    except rospy.ROSInterruptException:
        pass

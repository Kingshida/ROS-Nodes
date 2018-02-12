#include "ros/ros.h"
#include "geometry_msgs/Twist.h"

#include <iostream>
#include <fstream>
#include <string>

using namespace std;

ofstream outputFile;                                                            // csv file handle

void subCallback(const geometry_msgs::Twist& msg)
{
  ROS_INFO_STREAM("I heard: \n" <<msg);
  
  //Writing velocity data into file
  outputFile <<msg.linear.x <<"," << msg.linear.y <<"," << msg.linear.z  <<"," <<msg.angular.x <<"," <<msg.angular.y <<"," <<msg.angular.z <<endl;
}

int main(int argc, char **argv)
{
  //Creating FIle "vel_data.csv", saved in the workspace folder
  outputFile.open("vel_data.csv");
  outputFile <<"linear.x" <<"," << "linear.y" <<"," << "linear.z"  <<"," <<"angular.x" <<"," <<"angular.y" <<"," <<"angular.z" << endl;
  
  
  ros::init(argc, argv, "cpp_subscriber");                                      // Initialising ros node 
  ros::NodeHandle sub_h;                                                        // Creating node handle
  ros::Subscriber sub = sub_h.subscribe("turtle1/cmd_vel", 1000, subCallback);

  ros::spin();
  outputFile.close();                                                           // Save and close csv file, once the node is stopped
  return 0;
}
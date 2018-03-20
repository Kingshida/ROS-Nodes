#include "ros/ros.h"
#include "sensor_msgs/NavSatFix.h"


sensor_msgs::NavSatFix gps;

void subCallback(const sensor_msgs::NavSatFix& msg)
{
  ROS_INFO_STREAM("I heard: \n" <<msg);  
  gps = msg;
}

int main(int argc, char **argv)
{

  ros::init(argc, argv, "cpp_sub_pub");                                      // Initialising ros node 
  ros::NodeHandle node_h;                                                        // Creating node handle
  ros::Rate loop_rate(1);
  
  ros::Publisher pub = node_h.advertise<sensor_msgs::NavSatFix>("new_vel",1000);
  ros::Subscriber sub = node_h.subscribe("/fix", 1000, subCallback);
  
  
  while(ros::ok())
  {
    std::cout <<gps.latitude <<std::endl;
    pub.publish(gps);
    ros::spinOnce();
    loop_rate.sleep();
  }
    
  
  ros::spin();
  return 0;
}
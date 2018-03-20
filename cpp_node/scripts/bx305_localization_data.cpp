#include "ros/ros.h"
#include "ezls_msgs/LocalizationOutputData.h"
#include "sensor_msgs/NavSatFix.h"


sensor_msgs::NavSatFix gps_data;

void subCallback(const sensor_msgs::NavSatFix& msg)
{
  ROS_INFO_STREAM("I heard: \n" <<msg);  
  gps_data = msg;
}

ezls_msgs::LocalizationOutputData gps_to_utm(sensor_msgs::NavSatFix gps)
{
  ezls_msgs::LocalizationOutputData utmdata;
    
  return utmdata;
}

int main(int argc, char **argv)
{
  ezls_msgs::LocalizationOutputData utm;
  
  ros::init(argc, argv, "GPS_to_UTM");                                              // Initialising ros node 
  ros::NodeHandle node_h;                                                           // Creating node handle
  ros::Rate loop_rate(20);
  
  ros::Publisher pub = node_h.advertise<ezls_msgs::LocalizationOutputData>("utm_data",1000);   // Publishing to topic "utm_data"
  ros::Subscriber sub = node_h.subscribe("fix", 1000, subCallback);                 // tersus_bx305_node updates gps to topic "fix"
  
  
  while(ros::ok())
  {
    utm = gps_to_utm (gps_data);                                                          // Converting GPS to UTM
    pub.publish(utm);
    ros::spinOnce();
    loop_rate.sleep();
  }
    
  
  ros::spin();
  return 0;
}
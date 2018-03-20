#include "ros/ros.h"
#include "sensor_msgs/NavSatFix.h"
#include "sensor_msgs/NavSatStatus.h"
#include "sensor_msgs/TimeReference.h"

using namespace std;

int main(int argc, char **argv)
{
    ros::init(argc,argv, "")
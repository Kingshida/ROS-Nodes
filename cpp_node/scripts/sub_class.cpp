

#include "ros/ros.h"
#include "geometry_msgs/Twist.h"

using namespace std;

class sub_class
{
    public:
        void callback(const geometry_msgs::Twist& msg);
};

void sub_class::callback(const geometry_msgs::Twist& msg)
{
    ROS_INFO_STREAM("I heard: \n" <<msg);
}

int main(int argc, char **argv)                                     // argc -> argument count, argv -> argument vector 
{
    ros::init(argc, argv, "sub_veldata");                      // Initialising node 
    ros::NodeHandle n_handle;                                       // Creating node handle 
    
    sub_class sub;
    ros::Subscriber vel_sub = n_handle.subscribe("turtle1/cmd_vel", 1000, &sub_class::callback, &sub);  //vel_sub is Subscriber object
    
    ros::spin();

    
    return 0;
}
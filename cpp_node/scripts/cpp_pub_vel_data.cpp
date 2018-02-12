#include "ros/ros.h"
#include "geometry_msgs/Twist.h"

using namespace std;

int main(int argc, char **argv)                                     // argc -> argument count, argv -> argument vector 
{
    ros::init(argc, argv, "cpp_pub_vel_data");                      // Initialising publisher node 
    ros::NodeHandle n_handle;                                       // Creating node handle 
    ros::Publisher vel_pub = n_handle.advertise<geometry_msgs::Twist>("turtle1/cmd_vel", 1000);
    ros::Rate loop_rate(1);
    
    while(ros::ok())
    {
        geometry_msgs::Twist vel;
        vel.linear.x = double(rand())/double(RAND_MAX);             // Generating random numbers between [0,1]
        vel.angular.z = 2*double(rand())/double(RAND_MAX)-1;        // Generating random numbers between [-1,1]
        
        ROS_INFO_STREAM("\nVelocity is: \n"<<vel);
        vel_pub.publish(vel);
        
        ros::spinOnce();
        loop_rate.sleep();
    }
    
    return 0;
}

#include "ros/ros.h"
#include "std_msgs/String.h"

#include<sstream>

using namespace std;
using namespace ros;


int main(int argc,char **argv)
{
    init(argc, argv,"cpp_pub");
    NodeHandle pub_n;
    Publisher chatter_pub = pub_n.advertise<std_msgs::String>("chatter",1000);
    
    Rate loop_rate(10);
    
    int count =0;
    
    while(ok())
    {
        std_msgs::String msg;
        std::stringstream ss;
        ss << "hello world " << count;
        msg.data = ss.str();

        ROS_INFO("%s", msg.data.c_str());
        
        chatter_pub.publish(msg);

        spinOnce();

        loop_rate.sleep();
        ++count;
    }

    return 0;
}

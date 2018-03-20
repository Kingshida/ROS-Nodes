#include "ros/ros.h"
#include "ezls_msgs/LocalizationOutputData.h"
#include "sensor_msgs/NavSatFix.h"
#include "math.h"
#include <iostream>

const float f = (1/294.9786982), a = 6378206.4, phi_n = 0, k_n = 0.9996;
const float M_n = 0;
const float deg_rad = M_PI/180;

sensor_msgs::NavSatFix gps_data;

void subCallback(const sensor_msgs::NavSatFix& msg)
{
    ROS_INFO_STREAM("I heard: \n" <<msg);  
    gps_data = msg;
}

ezls_msgs::LocalizationOutputData gps_to_utm(sensor_msgs::NavSatFix gps)
{
    ezls_msgs::LocalizationOutputData utmdata;
    //std::cout << gps.latitude <<std::endl;
    float e_sqr,ed_sqr,R_m,N,T,C,A,M,x,y,k;
    float phi, lambda, lambda_n;                           // lat and longit in radians
    int c_zone, c_meridian, lat_band;
    
    
    phi = gps.latitude*deg_rad;
    lambda = gps.longitude*deg_rad;
    
    c_zone = ceil((gps.longitude+180)/6);
    c_meridian = (c_zone*6-180)-3;
    lambda_n = c_meridian*deg_rad;
        
    lat_band = ceil((gps.latitude+80)/8)+2;                 // adding 2 as band starts from 'C' 
    if (lat_band > 8 && lat_band <= 13)
        lat_band +=1;                                       // as 'I' is not included
    else if (lat_band > 13)             
        lat_band +=2;                                       // as 'O' is also not included
    
    e_sqr = (2*f)- pow(f,2);
    ed_sqr = e_sqr/(1-e_sqr);
    R_m = a*((1-e_sqr)/pow(1-(e_sqr*pow(sin(phi),2)),3/2));
    N = a/(sqrt(1-(e_sqr*pow(sin(phi),2)))); 
    T = pow(tan(phi),2);
    C = ed_sqr*pow(cos(phi),2);
    A = (lambda-lambda_n)*cos(phi);
    M = a*((1-(e_sqr/4)-(3*pow(e_sqr,2)/64)-(5*pow(e_sqr,3)/256))*phi\
        -((3*pow(e_sqr,1)/8)+(3*pow(e_sqr,2)/32)+(45*pow(e_sqr,3)/1024))*sin(2*phi)\
        +((15*pow(e_sqr,2)/256)+(45*pow(e_sqr,3)/1024))*sin(4*phi)-(35*pow(e_sqr,3)/3072*sin(6*phi)));
    
    
    x = 500000 + k_n*N*(A+((1-T+C)*pow(A,3)/6)+((5-18*T+pow(T,2)+72*C-58*ed_sqr)*pow(A,5)/120));
    y = k_n*(M-M_n+N*tan(phi)*((pow(A,2)/2)+(5-T+9*C+4*pow(C,2))*(pow(A,4)/24)+(61-58*T+pow(T,2)+600*C-330*ed_sqr)*(pow(A,6)/720)));

    utmdata.csInfo.cs = 2;
    utmdata.csInfo.zone = c_zone;
    utmdata.csInfo.latitudeBand = lat_band;
    
    utmdata.pose.pose.position.x = x;
    utmdata.pose.pose.position.y = y;
    utmdata.pose.pose.position.z = gps.altitude;

    return utmdata;
}

int main(int argc, char **argv)
{
    
    ezls_msgs::LocalizationOutputData utm;
    
    ros::init(argc, argv, "GPS_to_UTM");                                              // Initialising ros node 
    ros::NodeHandle node_h;                                                           // Creating node handle
    ros::Rate loop_rate(2);
    
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

#include <ros/ros.h>
#include <ros/time.h>
#include <geometry_msgs/Vector3.h>
#include <geometry_msgs/Twist.h>
#include "msg/12servo.msg"
#include "msg/indiv_servo.msg"

using namespace sajogi;

class motorControl
{
public:
    motorControl(ros::NodeHandle &nh):
    12servos_sub(nh.subscribe("msg/12servo.msg", 1000, &motorControl::control_CB, this))
    
}
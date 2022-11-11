#include <ros/ros.h>
#include <ros/time.h>
#include <geometry_msgs/Vector3.h>
#include <geometry_msgs/Twist.h>
#include "msg/12servo.msg"

using namespace sajogi;

// sajogi::servo <-- custom message
class sajogiMovement
{
public:
    sajogiMovement(ros::NodeHandle &nh):
    // pca9685_sub(nh.subscribe("/pca9685/angles")),
    // cmd_vel : geometry_msgs::Twist
    keyboard_sub(nh.subscribe("cmd_vel", 1000, &sajogiMovement::move_CB, this))
    pca9685_pub(nh.advertise<"geometry_msgs::Twist">("/servo_drive",10)),
    loop_rate(20)
    {
        initPCA9685Twist();
    }

    void spin()
    {
    while(ros::ok())
    {
        ros::spinOnce();
        pca9685_pub.publish(pca9685_msg);
        loop_rate.sleep();
    }
    }

    void initPCA9685Twist(void)
    {
        pca9685_msg.linear.x = 0; // throttle
        pca9685_msg.linear.y = 0;
        pca9685_msg.linear.z = 0;

        pca9685_msg.angular.x = 0; // let this decide direction(0: stop, 1 : fwd, 2 : bwd)
        pca9685_msg.angular.y = 0;
        pca9685_msg.angular.z = 0; // drive
    }

// rostopic pub servos_drive geometry_msgs/Twist "{linear: {x: 0.5}, angular: {z: -0.75}}
// need this kind of topic for each servo
    void move_CB(const geometry_msgs::Twist &cmd_vel)
    {
        if(!sajogi_move_received){
            initial_position = cmd_vel;
            sajogi_move_received = true
        }
        if(cmd_vel.angular.x == 1)
        {
            pca9685_msg.linear.x = cmd_vel.linear.x;
            pca9685_msg.angular.z = cmd_vel.angular.z;
        }
    }

private:
    ros::Subscriber keyboard_sub;
    ros::Publisher pca9685_pub;

    bool sajogi_move_received = false

    ros::NodeHandle nh;
    ros::Rate loop_rate;  

    geometry_msgs::Twist pca9685_msg
    geometry_msgs::Twist initial_position
}
    

int main(int argc, char **argv)
{
    ros::init(argc, argv, "sajogi_movement");
    ros::NodeHandle nh;
    sajogiMovement core(nh);
    core.spin();
    return 0;
}
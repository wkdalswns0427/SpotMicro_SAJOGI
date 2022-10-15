#include "pca9685_board/PCA9685_12Node.h"

int main(int argc, char** argv)
{
    ros::init(argc, argv, "pca9685_board");
    pca9685_board::PCA9685Node node;

    ros::spin();

    return 0;
}
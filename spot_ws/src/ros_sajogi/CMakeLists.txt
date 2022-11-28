cmake_minimum_required(VERSION 2.8.3)
project(ros_sajogi_movement)
add_compile_options(-std=c++11)

set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} -Wall")

find_library(wiringPi_LIB wiringPi)

find_package(catkin REQUIRED COMPONENTS
    roscpp
    std_msgs
    message_generation
)

add_message_files(FILES 12servo.msg)

generate_messages(DEPENDENCIES std_msgs)

catkin_package(CATKIN_DEPENDS message_runtime)

include_directories(include ${catkin_INCLUDE_DIRS})

set(SOURCES
    src/sajogi_move.cpp
    src/motorControl.cpp
    src/core.cpp
)

add_executable(ros_sajogi_movement ${SOURCES})
target_link_libraries(ros_sajogi_movement
    ${catkin_LIBRARIES}
    ${wiringPi_LIB}
)

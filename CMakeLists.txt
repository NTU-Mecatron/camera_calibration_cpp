cmake_minimum_required(VERSION 3.10)

# Project name
project(CameraCalibration)

# Set C++ standard
set(CMAKE_CXX_STANDARD 11)
set(CMAKE_CXX_STANDARD_REQUIRED True)

# Find OpenCV package
find_package(OpenCV REQUIRED)

# Add the executable
add_executable(camera_calibration camera_calibration.cpp)

# Link OpenCV libraries
target_link_libraries(camera_calibration ${OpenCV_LIBS})
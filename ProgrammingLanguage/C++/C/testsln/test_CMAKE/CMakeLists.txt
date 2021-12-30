# 设置运行此配置文件所需的CMake最低版本
cmake_minimum_required(VERSION 3.0.0)

# set the project name
project(PAOPIAN)

INCLUDE_DIRECTORIES($ENV{MdwDir}/API)
INCLUDE_DIRECTORIES($ENV{MdwDir}/LIB)

link_directories($ENV{MdwDir}/API)
link_directories($ENV{MdwDir}/LIB)

if(MSVC) 
    add_definitions(-D_CRT_SECURE_NO_WARNINGS) 
    add_definitions(-D_SILENCE_STDEXT_HASH_DEPRECATION_WARNINGS)
endif() 

set(CMAKE_CXX_FLAGS_DEBUG "${CMAKE_CXX_FLAGS_DEBUG} /MTd")

# add the executable(Need to be placed after LINK_DIRECTORIES )
add_executable(PAOPIAN test123.cpp)
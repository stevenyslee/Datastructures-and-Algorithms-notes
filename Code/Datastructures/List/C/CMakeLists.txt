cmake_minimum_required(VERSION 3.9)
set(SOURCE_FILES linked_list.c)
set(CMAKE_C_FLAGS "-DDEBUG -Wall")
add_executable(LLDebug ${SOURCE_FILES})
cmake_minimum_required(VERSION 3.18)
project(Image_Distorter LANGUAGES CXX CUDA)

set(CMAKE_C_COMPILER "cl")
set(CMAKE_CXX_COMPILER "cl")

if(NOT MSVC)
    message(FATAL_ERROR "This project requires MSVC (Visual Studio) as the compiler.")
endif()

add_executable(main src/main.cpp)

file(GLOB_RECURSE ALL_HEADERS
    "src/*.h"
    "src/*.hpp"
)


if(NOT CMAKE_BUILD_TYPE)
    set(CMAKE_BUILD_TYPE Release CACHE STRING "Build type" FORCE)
endif()

 message("CMAKE_SOURCE_DIR: ${CMAKE_SOURCE_DIR}")

# Optional: set executable output directory
set_target_properties(main PROPERTIES
    RUNTIME_OUTPUT_DIRECTORY "${CMAKE_SOURCE_DIR}/bin"
)

cmake_minimum_required(VERSION 3.10)
project(SDLBasicExample)

set(CMAKE_CXX_STANDARD 11)
set(CMAKE_CXX_STANDARD_REQUIRED True)

add_executable(sdl_basic src/main.cpp)

# Manually specify SDL3 include directory and libraries
# Adjust these paths to your actual SDL3 installation paths

set(SDL3_INCLUDE_DIR "${CMAKE_SOURCE_DIR}/include/")
set(SDL3_LIBRARY "${CMAKE_SOURCE_DIR}/lib")  # or .dll/.lib depending on platform
set(SDL3_SRC "${CMAKE_SOURCE_DIR}/src")  # or .dll/.lib depending on platform
set(SDL3_BIN "${CMAKE_SOURCE_DIR}/bin")  # or .dll/.lib depending on platform
set(SDL3_IMG "${CMAKE_SOURCE_DIR}/src/images/")  # or .dll/.lib depending on platform




file(GLOB_RECURSE ALL_HEADERS
    "${SDL3_SRC}/*.h"
    "${SDL3_SRC}/*.hpp"
)

file(GLOB_RECURSE ALL_DLLS
    "${SDL3_BIN}/*.dlls"
)

message("Found headers: ${ALL_HEADERS}")

target_include_directories(sdl_basic PUBLIC ${SDL3_SRC})
target_include_directories(sdl_basic PUBLIC ${SDL3_INCLUDE_DIR})
target_include_directories(sdl_basic PUBLIC ${SDL3_IMG})



# Find all .lib files in the libs directory
file(GLOB MY_LIB_FILES "${SDL3_LIBRARY}/*.a")
target_link_libraries(sdl_basic PRIVATE ${MY_LIB_FILES})
target_link_libraries(sdl_basic PRIVATE ${ALL_DLLS})


# Optional: set executable output directory
set_target_properties(sdl_basic PROPERTIES
    RUNTIME_OUTPUT_DIRECTORY "${CMAKE_SOURCE_DIR}/bin"
)

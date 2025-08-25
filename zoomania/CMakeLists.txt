cmake_minimum_required(VERSION 3.10)
project(SDLBasicExample)

set(CMAKE_CXX_STANDARD 11)
set(CMAKE_CXX_STANDARD_REQUIRED True)

add_executable(sdl_basic main.cpp)

# Manually specify SDL2 include directory and libraries
# Adjust these paths to your actual SDL2 installation paths

set(SDL2_INCLUDE_DIR "${CMAKE_SOURCE_DIR}/include/")
set(SDL2_LIBRARY "${CMAKE_SOURCE_DIR}/lib")  # or .dll/.lib depending on platform

target_include_directories(sdl_basic PUBLIC ${SDL2_INCLUDE_DIR})



# Find all .lib files in the specified directory
file(GLOB MY_LIB_FILES "${SDL2_LIBRARY}/*.a")

# Print the found files (for verification)
message("Found .lib files: ${MY_LIB_FILES}")

target_link_libraries(sdl_basic PRIVATE ${MY_LIB_FILES})

# Optional: set executable output directory
set_target_properties(sdl_basic PROPERTIES
    RUNTIME_OUTPUT_DIRECTORY "${CMAKE_SOURCE_DIR}/bin"
)

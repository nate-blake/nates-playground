cmake_minimum_required(VERSION 3.18)
project(Cuda_By_Example LANGUAGES CXX CUDA)
if(NOT MSVC)
    message(FATAL_ERROR "This project requires MSVC (Visual Studio) as the compiler.")
endif()

add_executable(hello_world src/chapter3/hello_world.cu)

file(GLOB_RECURSE ALL_HEADERS
    "src/*.h"
    "src/*.hpp"
)

# file(GLOB_RECURSE ALL_DLLS
#     "${SDL3_BIN}/*.dlls"
# )

if(NOT CMAKE_BUILD_TYPE)
    set(CMAKE_BUILD_TYPE Release CACHE STRING "Build type" FORCE)
endif()

 message("CMAKE_SOURCE_DIR: ${CMAKE_SOURCE_DIR}")
# target_include_directories(sdl_basic PUBLIC ${SDL3_SRC})
# target_include_directories(sdl_basic PUBLIC ${SDL3_INCLUDE_DIR})
# target_include_directories(sdl_basic PUBLIC ${SDL3_IMG})



# Find all .lib files in the libs directory
# file(GLOB MY_LIB_FILES "${SDL3_LIBRARY}/*.a")
# target_link_libraries(sdl_basic PRIVATE ${MY_LIB_FILES})
# target_link_libraries(sdl_basic PRIVATE ${ALL_DLLS})


# Optional: set executable output directory
set_target_properties(hello_world PROPERTIES
    RUNTIME_OUTPUT_DIRECTORY "${CMAKE_SOURCE_DIR}/bin"
)

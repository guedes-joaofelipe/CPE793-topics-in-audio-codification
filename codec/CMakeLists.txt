cmake_minimum_required(VERSION 3.20)
project(codec)

set(CMAKE_CXX_STANDARD 23)
set(CMAKE_POSITION_INDEPENDENT_CODE ON)

enable_testing()

include(ExternalProject)
set(EXTERNAL_INSTALL_LOCATION ${CMAKE_BINARY_DIR}/external)
ExternalProject_Add(googletest
        GIT_REPOSITORY https://github.com/google/googletest
        CMAKE_ARGS -DCMAKE_INSTALL_PREFIX=${EXTERNAL_INSTALL_LOCATION}
        )

include_directories(${EXTERNAL_INSTALL_LOCATION}/include)
link_directories(${EXTERNAL_INSTALL_LOCATION}/lib)


set(Headers
#        fill here
        )

set(Sources
        lib/bitrate/bitrate.cpp
        )

add_library(codec STATIC ${Sources} ${Headers})

add_subdirectory(test)
project(tests)

set(Sources myTest.cpp)

add_executable(tests ${Sources})
add_dependencies(tests googletest)
target_link_libraries(tests PUBLIC gtest_main)

add_test(
    NAME tests
    COMMAND tests
)
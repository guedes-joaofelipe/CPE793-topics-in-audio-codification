### Include the Google Test framework

1. Create a folder for Google Tests under the project root. Inside it, create another folder for the framework's files. In our example, it's `Google_tests` and `Google_tests/lib` folders respectfully.
2. Download Google Test from the official repository. Extract the contents of the googletest-master folder into `Google_tests/lib`.
3. Add a `CMakeLists.txt` file to the Google_tests folder (right-click it in the project tree and select New | `CMakeLists.txt`). Add the following lines:
```
project(Google_tests)
add_subdirectory(lib)
include_directories(${gtest_SOURCE_DIR}/include ${gtest_SOURCE_DIR})
```
4. In the root `CMakeLists.txt` script, add the `add_subdirectory(Google_tests)` line at the end and reload the project.
___
References: https://www.jetbrains.com/help/clion/unit-testing-tutorial.html#adding-framework
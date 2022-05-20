cmake_minimum_required(VERSION 3.5)
project(ichthus_xsens_driver)

if(NOT CMAKE_CXX_STANDARD)
  set(CMAKE_CXX_STANDARD 14)
  set(CMAKE_CXX_STANDARD_REQUIRED ON)
  set(CMAKE_CXX_EXTENSIONS OFF)
endif()
if(CMAKE_COMPILER_IS_GNUCXX OR CMAKE_CXX_COMPILER_ID MATCHES "Clang")
  add_compile_options(-Wall -Wextra -Wpedantic -Werror)
endif()

find_package(PythonLibs 3 REQUIRED)
find_package(ament_cmake_auto REQUIRED)
ament_auto_find_build_dependencies()

# find_package(Eigen3 REQUIRED)

# ament_python_install_package(${PROJECT_NAME} PACKAGE_DIR "scripts/")
# include_directories(
#   ${catkin_INCLUDE_DIRS}
# )

ament_auto_package(
  INSTALL_TO_SHARE
    cfg
    launch
)

install(PROGRAMS scripts/__init__.py scripts/ichthus_xsens_driver.py scripts/mtdef.py
                scripts/mtdevice.py scripts/mtnode.py DESTINATION lib/${PROJECT_NAME})

install(FILES DESTINATION share/${PROJECT_NAME})

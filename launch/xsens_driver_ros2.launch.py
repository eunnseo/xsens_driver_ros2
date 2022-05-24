import os
import launch
import ament_index_python

from launch import LaunchDescription
from launch_ros.actions import Node


def get_param_file(package_name, file_name):
  """Pass the given param file as a LaunchConfiguration."""
  file_path = os.path.join(
    ament_index_python.get_package_share_directory(package_name),
    'cfg',
    file_name)
  return launch.substitutions.LaunchConfiguration(
    'params', default=[file_path])


def generate_launch_description():
  """Generate launch description with multiple components."""

  # param = get_param_file(
  #   'xsens_driver_ros2',
  #   'frontend_default.param.yaml'
  # )

  return LaunchDescription([
    Node(
      package='xsens_driver_ros2',
      namespace='',
      executable='mtnode.py',
      name='mtnode',
      parameters=[
        {'device': 'auto'},
      ],
      output='screen'
    )
  ])

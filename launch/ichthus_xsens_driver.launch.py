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
  #   'ichthus_xsens_driver',
  #   'frontend_default.param.yaml'
  # )

  return LaunchDescription([
    Node(
      package='ichthus_xsens_driver',
      namespace='',
      executable='ichthus_xsens_driver',
      name='ichthus_xsens_driver'
      # parameters=[param]
    )
  ])

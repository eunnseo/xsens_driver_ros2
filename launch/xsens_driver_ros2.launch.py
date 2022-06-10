import os
import launch
import ament_index_python

from launch import LaunchDescription
from launch_ros.actions import Node


def generate_launch_description():
  """Generate launch description with multiple components."""

  return LaunchDescription([
    Node( # mtnode.py
      package='xsens_driver_ros2',
      namespace='',
      executable='mtnode.py',
      name='mtnode',
      parameters=[
        {'device': 'auto'},
        {'baudrate': 0},
        {'timeout': 0.002},
        {'initial_wait': 0.1},
        {'frame_id': '/imu'},
        {'frame_local': 'ENU'},
        {'no_rotation_duration': 0},
        {'angular_velocity_covariance_diagonal': [0.0004, 0.0004, 0.0004]},
        {'linear_acceleration_covariance_diagonal': [0.0004, 0.0004, 0.0004]},
        {'orientation_covariance_diagonal': [0.01745, 0.01745, 0.15708]},
      ],
      output='screen'
    )
    # Node( # mtdevice.py
    #   package='xsens_driver_ros2',
    #   namespace='',
    #   executable='mtdevice.py',
    #   name='mtdevice',
    #   parameters=[
    #     {'device': 'auto'},
    #     {'baudrate': 0},
    #     {'timeout': 0.002},
    #     {'initial_wait': 0.1},
    #     {'frame_id': '/imu'},
    #     {'frame_local': 'ENU'},
    #     {'no_rotation_duration': 0},
    #     {'angular_velocity_covariance_diagonal': [0.0004, 0.0004, 0.0004]},
    #     {'linear_acceleration_covariance_diagonal': [0.0004, 0.0004, 0.0004]},
    #     {'orientation_covariance_diagonal': [0.01745, 0.01745, 0.15708]},
    #   ],
    #   output='screen'
    # )
  ])

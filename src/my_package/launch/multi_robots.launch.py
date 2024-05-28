from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([
        Node(
            package='my_package',
            executable='image_saver_robot1',
            name='robot1_node',
            remappings=[
                ('camera/image_raw', 'robot1/camera/image_raw')
            ]
        ),
        # Node(
        #     package='my_package',
        #     executable='image_saver_robot1',
        #     name='robot2_node',
        #     remappings=[
        #         ('camera/image_raw', 'robot2/camera/image_raw')
        #     ]
        # )
    ])

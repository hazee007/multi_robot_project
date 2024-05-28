
# import os
# from launch import LaunchDescription
# from launch.actions import ExecuteProcess
# from ament_index_python.packages import get_package_share_directory
# from launch_ros.actions import Node

# def generate_launch_description():
#     world_file_name = 'test_zone.world'  # specify your world file
#     world = os.path.join(get_package_share_directory('my_package'), 'worlds', world_file_name)

#     # Define the robot's URDF file
#     turtlebot3_urdf = os.path.join(
#         get_package_share_directory('turtlebot3_description'),
#         'urdf',
#         'turtlebot3_waffle.urdf'
#     )

#     # Read the URDF file
#     # with open(turtlebot3_urdf, 'r') as inf:
#     #     robot_desc = inf.read()
# # /home/jide/ros2_ws/src/turtlebot3_simulations/turtlebot3_gazebo/models/turtlebot3_waffle/model.sdf
#     spawn_entity = Node(
#         package='gazebo_ros',
#         executable='spawn_entity.py',
#         output='screen',
#         arguments=['-entity', 'turtlebot3_waffle', '-file', '~/turtlebot3_simulations/turtlebot3_gazebo/models/turtlebot3_waffle/model.sdf']
#     )

#     return LaunchDescription([
#         spawn_entity
#     ])

#     # return LaunchDescription([
#     #     ExecuteProcess(
#     #         cmd=['gazebo', '--verbose', '-s', 'libgazebo_ros_init.so', world],
#     #         output='screen'),

#     #     # Spawn the first TurtleBot3
        

#     #     # SpawnEntity(
#     #     #     name='turtlebot3_1',
#     #     #     xml=robot_desc,
#     #     #     x=0,
#     #     #     y=0,
#     #     #     z=0
#     #     # ),

#     #     # # Spawn the second TurtleBot3
#     #     # SpawnEntity(
#     #     #     name='turtlebot3_2',
#     #     #     xml=robot_desc,
#     #     #     x=1,
#     #     #     y=0,
#     #     #     z=0
#     #     # ),

#     #     # # Spawn the third TurtleBot3
#     #     # SpawnEntity(
#     #     #     name='turtlebot3_3',
#     #     #     xml=robot_desc,
#     #     #     x=2,
#     #     #     y=0,
#     #     #     z=0
#     #     # ),
#     # ])




# # export GAZEBO_MODEL_PATH=${GAZEBO_MODEL_PATH}:${PWD}/install/my_package/share/my_package/models


import os
from launch import LaunchDescription
from launch.actions import ExecuteProcess
from ament_index_python.packages import get_package_share_directory
from launch_ros.actions import Node

def generate_launch_description():
    world_file_name = 'test_zone.world'  # specify your world file
    world = os.path.join(get_package_share_directory('my_package'), 'worlds', world_file_name)

    # Path to the TurtleBot3 model SDF file
    turtlebot3_model_path = os.path.join(
        get_package_share_directory('turtlebot3_simulations'),
        'turtlebot3_gazebo',
        'models',
        'turtlebot3_waffle',
        'model.sdf'
    )
    print(turtlebot3_model_path)
    return LaunchDescription([
        ExecuteProcess(
            cmd=['gazebo', '--verbose', '-s', 'libgazebo_ros_init.so', world],
            output='screen'),

        # Spawn the TurtleBot3 robot using the spawn_entity.py script
        Node(
            package='gazebo_ros',
            executable='spawn_entity.py',
            arguments=[
                '-entity', 'turtlebot3_waffle',
                '-file', turtlebot3_model_path,
                '-x', '0',
                '-y', '0',
                '-z', '0'
            ],
            output='screen'
        ),
    ])


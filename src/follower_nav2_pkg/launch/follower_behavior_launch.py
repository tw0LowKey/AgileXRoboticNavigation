from launch import LaunchDescription
from launch_ros.actions import Node
from ament_index_python.packages import get_package_share_directory
import os


def generate_launch_description():
    pkg_share = get_package_share_directory('follower_nav2_pkg')

    follower_config = os.path.join(pkg_share, 'config', 'follower_behavior_params.yaml')
    leader_config = os.path.join(pkg_share, 'config', 'leader_behavior_params.yaml')

    leader_behavior = Node(
        package='follower_nav2_pkg',
        executable='leader_behavior_node',
        name='leader_behavior_node',
        output='screen',
        parameters=[leader_config],
    )

    follower_behavior = Node(
        package='follower_nav2_pkg',
        executable='follower_behavior_node',
        name='follower_behavior_node',
        output='screen',
        parameters=[follower_config],
    )

    return LaunchDescription([
        leader_behavior,
        follower_behavior,
    ])
from setuptools import find_packages, setup

package_name = 'follower_nav2_pkg'

setup(
    name=package_name,
    version='0.0.1',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages', ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        ('share/' + package_name + '/launch', ['launch/follower_behavior_launch.py']),
        ('share/' + package_name + '/config', ['config/follower_behavior_params.yaml']),
        ('share/' + package_name + '/config', ['config/leader_behavior_params.yaml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='keyang',
    maintainer_email='keyang@todo.todo',
    description='Leader-follower behavior using Nav2 NavigateToPose',
    license='Apache-2.0',
    entry_points={
        'console_scripts': [
            'follower_behavior_node = follower_nav2_pkg.follower_behavior_node:main',
            'leader_behavior_node = follower_nav2_pkg.leader_behavior_node:main',
        ],
    },
)


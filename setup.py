from setuptools import find_packages, setup

package_name = 'robot_canopen_motor_pkg'

setup(
    name=package_name,
    version='0.0.1',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='shs',
    maintainer_email='minimirror1@gmail.com',
    description='ROS 2 package for CANopen motor control',
    license='Apache License 2.0',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'canopen_motor_node = robot_canopen_motor_pkg.canopen_motor_node:main',
        ],
    },
)

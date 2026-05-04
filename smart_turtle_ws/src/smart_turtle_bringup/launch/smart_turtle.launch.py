#!/usr/bin/env python3

# ------------------------- IMPORTS -------------------------
from launch import LaunchDescription
from launch_ros.actions import Node
from launch.substitutions import PathJoinSubstitution
from launch_ros.substitutions import FindPackageShare

# ------------------------- MAIN FUNCTION -------------------------
def generate_launch_description():
    ld = LaunchDescription()
    # ------------------------- LOAD PARAMETERS -------------------------
    param_config = PathJoinSubstitution([FindPackageShare('smart_turtle_bringup'),'config','turtle_param.yaml'])
    
    # ------------------------- NODES -------------------------
    turtle = Node(
        package="turtlesim",
        executable="turtlesim_node",
    )
    
    commander = Node(
        package="smart_turtle",
        executable="command_publisher",
        parameters=[param_config],
    )
    
    controller = Node(
        package="smart_turtle",
        executable="turtle_controller",
    )
    
    reset = Node(
        package="smart_turtle",
        executable="reset",
    )
    
    # ------------------------- ADD NODES TO LAUNCH -------------------------
    ld.add_action(turtle)
    ld.add_action(commander)
    ld.add_action(controller)
    ld.add_action(reset)
    
    return ld
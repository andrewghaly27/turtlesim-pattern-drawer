# Smart Turtle Controller

A ROS 2 Jazzy project built with **Turtlesim** to control a turtle using custom messages, parameters, services, and launch files. The system allows the turtle to draw different movement patterns such as circle, square, and spiral based on configurable runtime parameters.

## Project Overview

This project was developed as a final hands-on exercise after completing the ROS 2 Humble Foundations course. It applies core ROS 2 concepts by building a complete and interactive system organized into three packages: a logic/control package, an interface package, and a bringup package for launch and configuration.

## Workspace Structure

```bash
smart_turtle_ws/
├── src/
│   ├── smart_turtle_bringup/
│   │   ├── config/
│   │   │   └── turtle_param.yaml
│   │   ├── launch/
│   │   │   └── smart_turtle.launch.py
│   │   ├── package.xml
│   │   ├── CMakeLists.txt
│   │
│   ├── smart_turtle_interface/
│   │   ├── msg/
│   │   │   └── TurtleCommand.msg
│   │   ├── CMakeLists.txt
│   │   └── package.xml
│   │
│   └── smart_turtle/
│       ├── smart_turtle/
│       │   ├── __init__.py
│       │   ├── command_publisher.py
│       │   ├── turtle_controller.py
│       │   └── reset_node.py
│       ├── package.xml
│       ├── setup.py
│       ├── setup.cfg
│       └── resource/
│
├── docs/
│   ├── rqt_graph.png
│   ├── circle_demo.png
│   ├── square_demo.png
│   └── spiral_demo.png
│
├── .gitignore
└── README.md
```

## Packages

### `smart_turtle`
Contains the Python nodes that implement the system behavior.

- `command_publisher.py` reads parameters from the YAML file and publishes a custom message every 1 second on `/smart_turtle/command`.
- `turtle_controller.py` subscribes to `/smart_turtle/command`, interprets the pattern and speed, and publishes `Twist` commands to `/turtle1/cmd_vel`.
- `reset_node.py` sends `/reset` and `/clear` service requests every 10 seconds so the turtle returns to the start and redraws the shape.

### `smart_turtle_interface`
Defines the custom ROS 2 message used between the publisher and subscriber nodes.


### `smart_turtle_bringup`
Contains launch and configuration files needed to run the whole system together.

- `config/turtle_param.yaml` stores the selected movement pattern and speed.
- `launch/smart_turtle.launch.py` launches the Turtlesim node, controller node, command publisher node, and reset node together.

## Configuration

The project configuration is stored in `smart_turtle_bringup/config/turtle_param.yaml`. The project brief specifies two parameters: one for the movement pattern and one for the speed.


Supported patterns from the project brief are:

- `circle`
- `square`
- `spiral`
- `line`

## System Flow

1. `command_publisher.py` loads `pattern` and `speed` from the YAML config file.
2. It publishes a custom command message on `/smart_turtle/command` every 1 second.
3. `turtle_controller.py` receives that message and converts it into turtle velocity commands on `/turtle1/cmd_vel`.
4. `reset_node.py` calls `/reset` and `/clear` every 10 seconds so the drawing restarts cleanly.

## Build

```bash
cd ~/smart_turtle_ws
colcon build
source install/setup.bash
```

## Run

```bash
ros2 launch smart_turtle_bringup smart_turtle.launch.py
```

## Expected Behavior

After launching the project, the Turtlesim window should open automatically and the turtle should begin moving according to the configured pattern and speed.

The reset node should clear or restart the environment every 10 seconds, while all nodes communicate through ROS 2 topics and services as one integrated system.

## Changing Parameters

```bash
ros2 param set /command_publisher pattern "<choose-the-pattern>"
ros2 param set /command_publisher speed <choose-the-speed>
```

#!/usr/bin/env python3

import rclpy
from rclpy.node import Node
from smart_turtle_interfaces.msg import TurtleCommand

class Commander(Node):
    def __init__(self):
        super().__init__("command_publisher")
        
        self.declare_parameter("pattern","line")
        self.declare_parameter("speed",2.0)
        
        self.pattern_ = self.get_parameter("pattern").value
        self.speed_ = self.get_parameter("speed").value
        
        self.publisher_ = self.create_publisher(TurtleCommand, "/smart_turtle/command",1)
        self.timer_ = self.create_timer(1.0, self.publish_command)
        
        self.get_logger().info(f"The pattern the turtle is drawing is: {self.pattern_}, and its speed is: {self.speed_}")
        
    def publish_command(self):
        current_pattern = self.get_parameter("pattern").value
        current_speed = self.get_parameter("speed").value
        
        if current_pattern != self.pattern_:
            self.pattern_ = current_pattern
            self.get_logger().info(f"Changed the pattern to {self.pattern_}")
        
        if current_speed != self.speed_:
            self.speed_ = current_speed
            self.get_logger().info(f"Changed the turtle speed to {self.speed_}")
        
        msg = TurtleCommand()
        msg.pattern = self.pattern_
        msg.speed = self.speed_
        self.publisher_.publish(msg)
        
def main(args=None):
    rclpy.init(args=args)
    commander = Commander()
    rclpy.spin(commander)
    rclpy.shutdown()
    
if __name__ == "__main__":
    main()
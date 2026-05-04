#!/usr/bin/env python3

import time
import rclpy
from rclpy.node import Node
from smart_turtle_interfaces.msg import TurtleCommand
from geometry_msgs.msg import Twist
from std_srvs.srv import Empty

class TurtleController(Node):
    def __init__(self):
        super().__init__("turtle_controller")
        
        self.subscriber_ = self.create_subscription(TurtleCommand, "/smart_turtle/command", self.command_callback, 1)
        
        self.publisher_ = self.create_publisher(Twist, "/turtle1/cmd_vel", 1)
        self.timer_ = self.create_timer(0.1,self.command_publisher)
        
        self.restart_timer_server_ = self.create_service(Empty, "restart_timer", self.restart_timer)
        
        self.pattern_ = None
        self.speed_ = 0
        self.inc = 0
        
    def restart_timer(self, request: Empty.Request, response: Empty.Response):
        self.inc = 0
        self.timer_.reset()
        return response
        
    def command_callback(self,msg: TurtleCommand):
        self.pattern_ = msg.pattern
        self.speed_ = msg.speed
        
    def command_publisher(self):
        msg = Twist()
        if self.pattern_ == "line":
            msg.linear.x = self.speed_
            self.publisher_.publish(msg)
            
        elif self.pattern_ == "circle":
            msg.linear.x = self.speed_
            msg.angular.z = self.speed_
            self.publisher_.publish(msg)
            
        elif self.pattern_ == "square":
            msg.linear.x = self.speed_
            msg.angular.z = 0.0
            self.publisher_.publish(msg)
            time.sleep(1.0)
            msg.linear.x = 0.0
            msg.angular.z = 1.57
            self.publisher_.publish(msg)
            time.sleep(0.995)
        
        elif self.pattern_ == "spiral":
            self.inc += 0.1
            msg.angular.z = self.speed_
            if msg.linear.x <= 2.0:
                msg.linear.x = self.inc
                self.publisher_.publish(msg)
    
def main(args=None):
    rclpy.init(args=args)
    controller = TurtleController()
    rclpy.spin(controller)
    rclpy.shutdown()
    
if __name__ == "__main__":
    main()
#!/usr/bin/env python3

import rclpy
from rclpy.node import Node
from std_srvs.srv import Empty

class ResetNode(Node):
    def __init__(self):
        super().__init__("reset_node")
        
        self.reset_client_ = self.create_client(Empty, "/reset")
        self.clear_client_ = self.create_client(Empty, "/clear")
        self.restart_timer_client_ = self.create_client(Empty, "restart_timer")
        self.timer_ = self.create_timer(10.0, self.call_clients)
        
    def call_clients(self):
        while not self.reset_client_.wait_for_service(0.5):
            self.get_logger().info("Waiting for Reset Server")
            
        while not self.clear_client_.wait_for_service(0.5):
            self.get_logger().info("Waiting for Clear Server")
            
        while not self.restart_timer_client_.wait_for_service(0.5):
            self.get_logger().info("Waiting for Restart Server")
            
        request = Empty.Request()
        self.reset_client_.call_async(request)
        self.get_logger().info("Turtle Reset")
        self.clear_client_.call_async(request)
        self.get_logger().info("Turtle Cleared")
        self.restart_timer_client_.call_async(request)
        
def main(args=None):
    rclpy.init(args=args)
    node = ResetNode()
    rclpy.spin(node)
    rclpy.shutdown()
    
if __name__ == "__main__":
    main()
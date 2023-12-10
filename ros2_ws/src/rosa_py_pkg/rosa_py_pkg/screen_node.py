#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
 
 
class ScreenNode(Node):
    def __init__(self):
        super().__init__("screen")
        self.get_logger().info("Screen is active")
 
 
def main(args=None):
    rclpy.init(args=args)
    node = ScreenNode()
    rclpy.spin(node)
    rclpy.shutdown()
 
 
if __name__ == "__main__":
    main()

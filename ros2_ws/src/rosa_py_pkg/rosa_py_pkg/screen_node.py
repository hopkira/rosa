#!/usr/bin/env python3
import rclpy
from rclpy.node import Node

# from example_interfaces.msg import String
from rosa_interfaces.msg import ScreenStatus
 
class ScreenNode(Node):
    def __init__(self):
        super().__init__("screen")
        self.subscriber_ = self.create_subscription(
            ScreenStatus, "screen_state", self.callback_screen_state, 10)
        self.get_logger().info("Screen started")

    def callback_screen_state(self, msg):
        text = "Speed: " + str(msg.speed) + ", Red: " + str(msg.colour.red) + ", Blue: " + str(msg.colour.blue) + ", Green: " + str(msg.colour.green)
        self.get_logger().info(text)
 
def main(args=None):
    rclpy.init(args=args)
    node = ScreenNode()
    rclpy.spin(node)
    rclpy.shutdown()
 
 
if __name__ == "__main__":
    main()

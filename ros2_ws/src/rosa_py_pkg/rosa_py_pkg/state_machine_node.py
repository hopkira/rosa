#!/usr/bin/env python3
import random

import rclpy
from rclpy.node import Node

# from example_interfaces.msg import String
from rosa_interfaces.msg import ScreenStatus
 
class StateMachineNode(Node):
    def __init__(self):
        super().__init__("state_machine")
        self.publisher_ = self.create_publisher(ScreenStatus, "screen_state", 10)
        self.get_logger().info("State Machine started")
        self.create_timer(1.0, self.publish_state)
        self.get_logger().info("Staltus publisher started")

    def publish_state(self):
        # msg_string = "Hello " + str(self.counter_)
        msg = ScreenStatus()
        msg.speed = random.randint(-10, 10)
        msg.colour.red = random.randint(0, 255)
        msg.colour.green = random.randint(0, 255)
        msg.colour.blue = random.randint(0, 255)
        self.publisher_.publish(msg)

def main(args=None):
    rclpy.init(args=args)
    node = StateMachineNode()
    rclpy.spin(node)
    rclpy.shutdown()
 
 
if __name__ == "__main__":
    main()

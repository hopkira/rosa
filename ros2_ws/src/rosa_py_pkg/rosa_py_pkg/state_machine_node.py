#!/usr/bin/env python3
import rclpy
from rclpy.node import Node

from example_interfaces.msg import String
 
class StateMachineNode(Node):
    def __init__(self):
        super().__init__("state_machine")
        self.publisher_ = self.create_publisher(String, "screen_state", 10)
        self.counter_ = 0
        self.get_logger().info("State Machine started")
        self.create_timer(1.0, self.publish_state)

    def publish_state(self):
        msg_string = "Hello " + str(self.counter_)
        msg = String()
        msg.data = msg_string
        self.publisher_.publish(msg)
        self.counter_ += 1

def main(args=None):
    rclpy.init(args=args)
    node = StateMachineNode()
    rclpy.spin(node)
    rclpy.shutdown()
 
 
if __name__ == "__main__":
    main()

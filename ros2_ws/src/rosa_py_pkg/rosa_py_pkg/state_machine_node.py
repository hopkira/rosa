#!/usr/bin/env python3
import random
from functools import partial

import rclpy
from rclpy.node import Node

# from example_interfaces.msg import String
from rosa_interfaces.msg import ScreenStatus
from rosa_interfaces.srv import TextToSpeech
 
class StateMachineNode(Node):
    def __init__(self):
        super().__init__("state_machine")
        self.publisher_ = self.create_publisher(ScreenStatus, "screen_state", 10)
        self.get_logger().info("State Machine started")
        self.create_timer(1.0, self.publish_state)
        self.get_logger().info("Status publisher started")
        self.tts_client = self.create_client(TextToSpeech,"text_to_speech")
        while not self.tts_client.wait_for_service(1.0):
            self.get_logger().warn("Creating client for text to speech server")
        self.get_logger().info("Client connected to text to speech server")

    def publish_state(self):
        # msg_string = "Hello " + str(self.counter_)
        msg = ScreenStatus()
        msg.speed = random.randint(-10, 10)
        msg.colour.red = random.randint(0, 255)
        msg.colour.green = random.randint(0, 255)
        msg.colour.blue = random.randint(0, 255)
        self.speak("Changing colour")
        self.publisher_.publish(msg)
    
    def speak(self, text):
        request = TextToSpeech.Request()
        request.text = text
        future = self.tts_client.call_async(request)
        future.add_done_callback(partial(self.callback_call_tts, text = text))

    def callback_call_tts(self, future, text):
        try:
            response = future.result()
            self.get_logger().info(str("Speech server said - " + text))
        except Exception as e:
            self.get_logger().error("Text to speech service call failed %r" % (e,))

def main(args=None):
    rclpy.init(args=args)
    node = StateMachineNode()
    rclpy.spin(node)
    rclpy.shutdown()
 

if __name__ == "__main__":
    main()

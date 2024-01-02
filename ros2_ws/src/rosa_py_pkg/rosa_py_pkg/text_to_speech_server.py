#!/usr/bin/env python3
import rclpy
from rclpy.node import Node

# from example_interfaces.msg import String
from rosa_interfaces.srv import TextToSpeech

class TextToSpeechNode(Node):
    def __init__(self):
        super().__init__("text_to_speech_server")
        self.server_ = self.create_service(TextToSpeech, "text_to_speech", self.callback_text_to_speech)
        self.get_logger().info("Text to speech server has been started")
    
    def callback_text_to_speech(self, request, response):
        self.get_logger().info(str("Text to speech server  said: " + request.text))
        response.accepted = True
        return response 
 
def main(args=None):
    rclpy.init(args=args)
    node = TextToSpeechNode()
    rclpy.spin(node)
    rclpy.shutdown()
 
 
if __name__ == "__main__":
    main()
  
#! /usr/bin/env python

import sys
import rclpy
from rclpy.node import Node

from sensor_msgs.msg import Image
import cv2
from cv_bridge import CvBridge

class ImagePublisher(Node):
    def __init__(self):
        super().__init__('image_publisher')
        self.publisher_ = self.create_publisher(Image, '/image_raw', 10)
        timer_period = 0.5
        self.timer = self.create_timer(timer_period, self.publish_image)
        self.bridge = CvBridge()


    def publish_image(self):
        img = cv2.imread("/Humble/ros2_ws/src/ros2_template/img0020.jpg")
        img_msg = self.bridge.cv2_to_imgmsg(img, encoding="bgr8")

        self.publisher_.publish(img_msg)
        self.get_logger().info('Image published')


def main(args=None):
    rclpy.init(args=args)
    image_publisher = ImagePublisher()
    rclpy.spin(image_publisher)
    
    image_publisher.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main(sys.argv)
#! /usr/bin/env python

import sys
import rclpy
from rclpy.node import Node

from sensor_msgs.msg import Image
import cv2
from cv_bridge import CvBridge


class ImageSubscriber(Node):
    def __init__(self):
        super().__init__('image_subscriber')
        self.publisher_ = self.create_publisher(Image, 'image_raw', 10)
        timer_period = 0.1
        self.timer = self.create_timer(timer_period, self.publish_image)
        self.bridge = CvBridge()


    def publish_image(self):
        img = cv2.imread()
        img_msg = self.bridge.cv2_to_imgmsg(img, encoding="bgr8")

        self.publisher_.publish(img_msg)
        self.get_logger().info('Image published')

    def timer_callback(self):
        pass


def main(args):
    pass

if __name__ == '__main__':
    main(sys.argv)

    
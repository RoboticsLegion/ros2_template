
import sys
import rclpy
from rclpy.node import Node


class ImagePublisher(Node):
    def __init__(self):
        super().__init__('image_publisher')
        pass


    def timer_callback(self):
        pass


def main(args):
    pass

if __name__ == '__main__':
    main(sys.argv)
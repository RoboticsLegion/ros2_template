#! /usr/bin/env python

import rclpy
from rclpy.node import Node

from std_msgs.msg import String, Int16


class MinimalSubscriber(Node):

    def __init__(self):
        super().__init__('minimal_subscriber')
        self.subscription_msg = self.create_subscription(String, '/pkg/status', self.listener_callback_msg, 10)
        self.subscription_msg

        self.subscription_cmd = self.create_subscription(Int16, '/pkg/cmd_vel', self.listener_callback_cmd, 10)
        self.subscription_cmd 

    def listener_callback_msg(self, msg):
        self.get_logger().info('I heard: "%s"' % msg.data)

    def listener_callback_cmd(self, msg):
        self.get_logger().info('Cmd:  "%s"' % msg.data)


def main(args=None):
    rclpy.init(args=args)

    minimal_subscriber = MinimalSubscriber()

    rclpy.spin(minimal_subscriber)

    minimal_subscriber.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
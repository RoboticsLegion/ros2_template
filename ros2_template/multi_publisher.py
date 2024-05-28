import rclpy
from rclpy.node import Node

from std_msgs.msg import String, Int16


class MultiPublisher(Node):

    def __init__(self):
        super().__init__('multi_publisher')
        self.publisher_status = self.create_publisher(String, '/pkg/status', 10)
        self.publisher_speed = self.create_publisher(Int16, '/pkg/cmd_vel', 10)
        timer_period = 0.5  # seconds
        self.timer = self.create_timer(timer_period, self.timer_callback)
        self.i = 0

    def timer_callback(self):
        msg = String()
        msg.data = 'Hello World: %d' % self.i

        cmd_msg = Int16()
        cmd_msg.data = self.i

        self.publisher_status.publish(msg)
        self.publisher_speed.publish(cmd_msg)
        
        self.get_logger().info('Publishing: "%s"' % msg.data)
        self.i += 1


def main(args=None):
    rclpy.init(args=args)

    multi_publisher = MultiPublisher()

    rclpy.spin(multi_publisher)

    multi_publisher.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
import time
from rclpy.node import Node
from std_msgs.msg import Int8
from std_srvs.srv import Empty


class TestNode(Node):

    def __init__(self):
        super().__init__("test_node")
        self.pub = self.create_publisher(Int8, "test_topic", 1)
        self.create_service(Empty, "test_service", self.srv_callback)

    def srv_callback(self, req, res):
        time.sleep(1.0)
        return res

    def publish_topic(self, i: int):
        if not isinstance(i, int):
            i = 0
        self.pub.publish(Int8(data=i))

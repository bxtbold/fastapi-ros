import rclpy
import uvicorn
from .backend.server import MyApp
from .test_node import TestNode


def main():
    import threading

    rclpy.init()
    node = TestNode()
    my_app = MyApp(node)

    try:
        thread = threading.Thread(target=rclpy.spin, args=(node,), daemon=True)
        thread.start()
        uvicorn.run(my_app.app, port=9091)
    except KeyboardInterrupt as e:
        pass
    finally:
        rclpy.shutdown()
        thread.join()


if __name__ == "__main__":
    main()

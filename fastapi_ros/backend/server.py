from fastapi import FastAPI, Depends
from rclpy.node import Node
from pydantic import BaseModel


class Response(BaseModel):
    msg: str


class MyApp:

    def __init__(self, node: Node):
        self.app = FastAPI()
        self.node = node
        self.setup_routes()

    def get_node(self):
        return self.node

    def setup_routes(self):
        @self.app.get("/")
        def read_root():
            return {"msg": "Success"}

        @self.app.get("/publish", response_model=Response)
        async def publish_topic():
            try:
                self.node.publish_topic(0)
                msg = "Success"
            finally:
                return {
                    "msg": msg
                }

        @self.app.get("/publish/{number}", response_model=Response)
        async def publish_topic(number: int):
            try:
                self.node.publish_topic(number)
                msg = "Success"
            except Exception as e:
                msg = str(e)
            finally:
                return {
                    "msg": msg
                }

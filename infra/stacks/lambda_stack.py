from functions.hello_world.config import HelloWorldConfig
from functions.rag.ask_question.config import AskQuestionConfig
from aws_cdk import Stack
from constructs import Construct
from infra.services import Services


class LambdaStack(Stack):
    def __init__(self, scope: Construct, context, **kwargs) -> None:

        super().__init__(scope, f"{context.name}-Lambda-Stack", **kwargs)

        self.services = Services(self, context)

        # HelloWorld
        HelloWorldConfig(self.services)

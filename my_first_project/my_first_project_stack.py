from aws_cdk import (
    # Duration,
    Stack,
    # aws_sqs as sqs,
)
from aws_cdk import cloudformation_include as cfn_inc
from constructs import Construct
#from aws_cdk import Stack
from aws_cdk.pipelines import CodePipeline, CodePipelineSource, ShellStep


class MyFirstProjectStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        template = cfn_inc.CfnInclude(self, "Template",  
            template_file="migration_template.yaml")
        
        

        # The code that defines your stack goes here

        # example resource
        # queue = sqs.Queue(
        #     self, "MyFirstProjectQueue",
        #     visibility_timeout=Duration.seconds(300),
        # )

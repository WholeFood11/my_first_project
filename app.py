#!/usr/bin/env python3
import os

import aws_cdk as cdk
from aws_cdk.pipelines import CodePipeline, CodePipelineSource, ShellStep
from my_first_project.my_first_project_stack import MyFirstProjectStack
from my_first_project.my_pipeline_stack import MyPipelineStack

app = cdk.App()
MyFirstProjectStack(app, "WFM-S3",
    # If you don't specify 'env', this stack will be environment-agnostic.
    # Account/Region-dependent features and context lookups will not work,
    # but a single synthesized template can be deployed anywhere.

    # Uncomment the next line to specialize this stack for the AWS Account
    # and Region that are implied by the current CLI configuration.

    #env=cdk.Environment(account=os.getenv('CDK_DEFAULT_ACCOUNT'), region=os.getenv('CDK_DEFAULT_REGION')),

    # Uncomment the next line if you know exactly what Account and Region you
    # want to deploy the stack to. */

    env=cdk.Environment(account='054548226963', region='us-east-2'),

    # For more information, see https://docs.aws.amazon.com/cdk/latest/guide/environments.html
    )

MyPipelineStack(app, "MyPipelineStack", 
    env=cdk.Environment(account='054548226963', region='us-east-2')
)


app.synth()

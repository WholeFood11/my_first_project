import aws_cdk as cdk
from constructs import Construct
from aws_cdk.pipelines import CodePipeline, CodePipelineSource, ShellStep
from my_first_project.my_pipeline_app_stage import MyPipelineAppStage
from aws_cdk.pipelines import ManualApprovalStep

class MyPipelineStack(cdk.Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        pipeline =  CodePipeline(self, "Pipeline", 
                        pipeline_name="MyPipeline",
                        synth=ShellStep("Synth", 
                            input=CodePipelineSource.git_hub("WholeFood11/my_first_project", "master"),
                            commands=["npm install -g aws-cdk", 
                                "python -m pip install -r requirements.txt", 
                                "cdk synth"]
                        )
                    )
        
        pipeline.add_stage(MyPipelineAppStage(self, "Beta",
            env=cdk.Environment(account='054548226963', region='us-east-2')))
        
        testing_stage = pipeline.add_stage(MyPipelineAppStage(self, "Testing",
        env=cdk.Environment(account='054548226963', region='us-east-2')))

        testing_stage.add_post(ManualApprovalStep('Please review and provide approval'))
        
        europe_wave = pipeline.add_wave("Europe")
        europe_wave.add_stage(MyPipelineAppStage(self, "Ireland",
            env=cdk.Environment(account='054548226963',region="eu-west-1")
        ))
        europe_wave.add_stage(MyPipelineAppStage(self, "Paris",
            env=cdk.Environment(account='054548226963',region="eu-west-3")
        ))

        

        
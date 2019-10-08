import boto3
from time import sleep

cfn = boto3.client('cloudformation')

try:
    # Get base stack outputs.
    stack_id = cfn.describe_stacks(StackName='MinecraftInstance')['Stacks'][0]['StackId']
    cfn.delete_stack(StackName=stack_id)
    print(f"Deleting Stack: {stack_id}")
except Exception as e:
    print('Something went wrong! Make sure to manually delete the stack!')
    print(e)
    exit(-1)

"""Starts a new Minecraft Server by launching the instance.json stack."""

import boto3
from time import sleep
import os

cfn = boto3.client('cloudformation')

# Get base stack outputs.
try:
    outputs = cfn.describe_stacks(StackName='MinecraftBase')['Stacks'][0]['Outputs']
except Exception as e:
    print('Something went wrong!')
    print(e)
    exit(-1)

parameters = []
for output in outputs:
    parameters.append({
        'ParameterKey': output['OutputKey'],
        'ParameterValue': output['OutputValue'],
        'UsePreviousValue': False
    })

# Read stack body...depends where the script is called.
if os.path.exists('.\\cfn\\instance.json') and os.path.isfile('.\\cfn\\instance.json'):
    with open('.\\cfn\\instance.json') as file_obj:
        template_data = file_obj.read()
elif os.path.exists('..\\cfn\\instance.json') and os.path.isfile('..\\cfn\\instance.json'):
    with open('..\\cfn\\instance.json') as file_obj:
        template_data = file_obj.read()
else:
    print('Unable to find path to instance.json')
    exit(-1)

# Launch new stack.
try:
    stack_id = cfn.create_stack(StackName='MinecraftInstance',
                                TemplateBody=template_data,
                                Parameters=parameters,
                                TimeoutInMinutes=5,
                                Capabilities=['CAPABILITY_NAMED_IAM'])['StackId']
except Exception as e:
    print('Something went wrong!')
    print(e)
    exit(-1)

try:
    stack_status = cfn.describe_stacks(StackName=stack_id)['Stacks'][0]['StackStatus']
    print(f"Stack Status: {stack_status}")

    while stack_status not in ['CREATE_FAILED',
                            'CREATE_COMPLETE',
                            'ROLLBACK_COMPLETE',
                            'DELETE_COMPLETE']:
        sleep(3)
        stack_status = cfn.describe_stacks(StackName=stack_id)['Stacks'][0]['StackStatus']
        print(f"Stack Status: {stack_status}")
except Exception as e:
    print('Something went wrong!')
    print(e)
    exit(-1)

# Print outputs.
print('Complete!')
print(f"Stack ID: {stack_id}")
try:
    outputs = cfn.describe_stacks(StackName=stack_id)['Stacks'][0]['Outputs']
    for output in outputs:
        print(f"{output['OutputKey']}: {output['OutputValue']}")
except Exception as e:
    print('Something went wrong!')
    print(e)
    exit(-1)

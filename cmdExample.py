import click
import boto3
import json
from datetime import date, datetime

def json_serial(obj):
    """JSON serializer for objects not serializable by default json code"""

    if isinstance(obj, (datetime, date)):
        return obj.isoformat()
    raise TypeError ("Type %s not serializable" % type(obj))

@click.command()
def envCreate():
    print("@ create environment!")

@click.command()
@click.argument('stackname')
def envRead(stackname):
    client = boto3.client('cloudformation')
    for stack in client.list_stacks()['StackSummaries']:
        print('{0}:{1}'.format(stack['StackName'], stack['StackId']))

    print("@ read environment")


@click.command()
def getStacks():
    client = boto3.client('cloudformation')
    stacks = client.describe_stacks()


@click.command()
def envUpdate():
    print("@update environemnt")

@click.command()
def envDelete():
    print("@ delete environment") 

@click.group()
def doStuff():
    pass

doStuff.add_command(envCreate)
doStuff.add_command(envRead)
doStuff.add_command(envUpdate)
doStuff.add_command(envDelete)


if __name__ == '__main__':
    doStuff()
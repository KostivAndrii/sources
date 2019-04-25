import boto3
import json
import os
dynamodb = boto3.resource('dynamodb')
table_name=os.environ['myTable']
table = dynamodb.Table(table_name)

def add(event, context):
    try:
        table.put_item(Item=event)
        resp = {
            'message': 'Batch details added successfully'
        }
        return json.dumps(resp)
    except Exception as e:
        response = {
            'statusCode': 500,
            'message': 'Batch details not found'
        }
        raise Exception(json.dumps(response))

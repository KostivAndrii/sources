import boto3
import json
import os
from boto3.dynamodb.conditions import Attr
from boto3.dynamodb.conditions import Key
import botocore

dynamodb = boto3.resource('dynamodb')
table_name=os.environ['myTable']
table = dynamodb.Table(table_name)

def add(event, context):
    try:
        try:

         resp = table.update_item(
            Key={
                'year': event['year'],
                'time_stamp': event['time_stamp']
            },
            UpdateExpression="set batch_details = list_append(batch_details, :b)",
            ExpressionAttributeValues={
                ':b': event['batches']
            },
            ConditionExpression='attribute_exists(batch_details)'
         )
         resp= {
            'message': 'Batch_details added successfully'
         }
         return json.dumps(resp)
        except botocore.exceptions.ClientError as e:
         resp = table.update_item(
            Key={
                'year': event['year'],
                'time_stamp': event['time_stamp']
            },
            UpdateExpression="set batch_details = :b",
            ExpressionAttributeValues={
                ':b': event
            },
            ConditionExpression='attribute_exists(time_stamp)'
        )
        response ={
            'message': 'Batch_details added successfully'
        }
        return json.dumps(response)
    except Exception:
        response = {
            'responseCode': 500,
            'message': 'Error adding batch details '
        }
        return json.dumps(response)

import boto3
import json
import os
from boto3.dynamodb.conditions import Attr
from boto3.dynamodb.conditions import Key

dynamodb = boto3.resource('dynamodb')
table_name=os.environ['TABLE_NAME']
table = dynamodb.Table(table_name)

def add(event,context):
        course_content  = event['course_id']
        response = table.query(
            KeyConditionExpression=Key('course_id').eq(course_content)
        )
        items = response.get('Items')

        response = {
            'body':response['Items'],
            'message': 'Success',
            'statusCode':200
        }
        return json.dumps(response)

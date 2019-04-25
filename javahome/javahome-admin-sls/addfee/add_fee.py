import boto3
import json
import os
from boto3.dynamodb.conditions import Attr
from boto3.dynamodb.conditions import Key
import botocore
dynamodb = boto3.resource('dynamodb')
table_name=os.environ['myTable']
table = dynamodb.Table(table_name)


def add(event,context):

    year  = event['year']
    time_stamp=event['time_stamp']
    del event['year']
    del event['time_stamp']

    try:

        resp = table.update_item(
            Key={
                'year': year,
                'time_stamp': time_stamp
            },
            UpdateExpression="set fee.payments = list_append(fee.payments, :payments)",
            ExpressionAttributeValues={
                ':payments': event['payments']
            },
            ConditionExpression='attribute_exists(fee)'
        )
        response = {
            'statusCode': 200,
            'message': 'Fee updated successfully'
        }
        return json.dumps(response)
    except botocore.exceptions.ClientError as e:
        try:
            resp = table.update_item(
            Key={
                'year': year,
                'time_stamp': time_stamp
            },
            UpdateExpression="set fee = :fee",
            ExpressionAttributeValues={
                ':fee': event
            },
            ConditionExpression='attribute_exists(time_stamp)'

            )
            resp = {
                'statusCode': 200,
                'message': 'Fee updated successfully'
             }
            return json.dumps(resp)
        except Exception as e:
            response={
            'statusCode': 500,
            'message': 'Updated Fee is incorrect'

        }
            raise Exception(json.dumps(response))

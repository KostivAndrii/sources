import boto3
import json
import os
from datetime import datetime
import re

dynamodb = boto3.resource('dynamodb')
table_name=os.environ['TABLE_NAME']
table = dynamodb.Table(table_name)
sns_client =  boto3.client('sns', 'us-east-1')
jh_sns_arn = 'arn:aws:sns:us-east-1:353848682332:javahome'

def add(event, context):

    try:
        validate_number(event['mobile'])
        numbe_with_code = event['country_code'] + event['mobile']
        del event['country_code']
        timestamp=datetime.now()
        timestamp=(timestamp.strftime("%d-%b-%Y %H:%M:%S:%f"))
        now=datetime.now()
        year=(now.strftime("%Y"))
        record = event
        record['year'] = year
        record['time_stamp'] = timestamp
        record['mobile'] = numbe_with_code
        table.put_item(
            Item=record
        )

        # subscribe_to_sns(event['mobile'])
        resp = {
            'statusCode':200,
            'message': 'Student added successfully'
        }
        return json.dumps(resp)
    except Exception as e:
        response = {
            'statusCode': 500,
            'message': str(e)
        }
        raise Exception(json.dumps(response))

def subscribe_to_sns(mobile):

    response = sns_client.subscribe(
        TopicArn=jh_sns_arn,
        Protocol="sms",
        Endpoint=mobile
    )


def validate_number(mobile):
    if not re.match(r'^\d{10}$',mobile):
        raise Exception("Invalid Mobile Number")


import json
import urllib.parse
import boto3


s3 = boto3.client('s3')
import boto3
import json

dynamodb = boto3.resource('dynamodb')

table = dynamodb.Table('s3_demo')


def lambda_handler(event, context):
    print(event)
    bucket = event['Records'][0]['s3']['bucket']['name']
    key = urllib.parse.unquote_plus(event['Records'][0]['s3']['object']['key'], encoding='utf-8')
    try:
        response = s3.get_object(Bucket=bucket, Key=key)
        print("CONTENT TYPE: " + response['ContentType'])
        data = json.loads(response['Body'].read())
        
        table.put_item(
            TableName='s3_demo',
            Item=data
            )
        print(data)
    except Exception as e:
        print(e)
        print('Error getting object {} from bucket {}. Make sure they exist and your bucket is in the same region as this function.'.format(key, bucket))
        raise e

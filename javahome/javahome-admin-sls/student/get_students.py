import boto3
import json
import os
from boto3.dynamodb.conditions import Attr
from boto3.dynamodb.conditions import Key

dynamodb = boto3.resource('dynamodb')
table_name=os.environ['myTable']
table = dynamodb.Table(table_name)


def add(event,context):
    try:
        search_expr = search_students(event)
        if search_expr is not None:
            students_resp = table.scan(FilterExpression=search_expr)
        else:
            students_resp = table.scan()
        return {
            'body': students_resp['Items']
        }

    except Exception as e:
        response = {
            'responseCode': 500,
            'message': str(e)
        }
        raise Exception(json.dumps(response))


# Build Search Criteria Expression
def search_students(criteria):
    search_exp = None
    if 'search_fields' in criteria:
        for field in criteria['search_fields']:
            # Build Courses Criteria
            if 'courses' in field:
                courses = field['courses']
                search_exp = Attr('courses').contains(courses[0])
                for course in courses:
                    search_exp = search_exp | Attr('courses').contains(course)
            elif 'mobile' in field:
                if search_exp:
                    search_exp = search_exp | Attr('mobile').contains(field['mobile'])
                else:
                    search_exp = Attr('mobile').contains(field['mobile'])
            elif 'prefferd_timings' in field:
                prefferd_timings = field['prefferd_timings']
                search_exp = Attr('prefferd_timings').contains(prefferd_timings[0])
                for prefferd_timing in prefferd_timings:
                    search_exp = search_exp | Attr('prefferd_timings').contains(prefferd_timing)
    return search_exp

import logging
import json
logger = logging.getLogger()
logger.setLevel(logging.DEBUG)


def close(session_attributes, fulfillment_state, message):
    response = {
        'sessionAttributes': session_attributes,
        'dialogAction': {
            'type': 'Close',
            'fulfillmentState': fulfillment_state,
            'message': message
        }
    }

    return response


def delegate(session_attributes, slots):
    return {
        'sessionAttributes': session_attributes,
        'dialogAction': {
            'type': 'Delegate',
            'slots': slots
        }
    }


def elicit_slot(session_attributes, intent_name, slots, slot_to_elicit, message, response_card):
    return {
        'sessionAttributes': session_attributes,
        'dialogAction': {
            'type': 'ElicitSlot',
            'intentName': intent_name,
            'slots': slots,
            'slotToElicit': slot_to_elicit,
            'message': message,
            'responseCard': response_card
        }
    }


def build_validation_result(is_valid, violated_slot, message_content):
    return {
        'isValid': is_valid,
        'violatedSlot': violated_slot,
        'message': {'contentType': 'PlainText', 'content': message_content}
    }


def validate_course_enquiry(name, phone, courses):
    if not name:
        return build_validation_result(False, 'Name',
                                       'I will help you with course details, What\'s your name?')
    elif not phone:
        return build_validation_result(False, 'Phone',
                                       'Whats\'s your phone number?')
    elif not courses:
        return build_validation_result(False, 'CourseName',
                                       'Which course you are looking for?')
    return build_validation_result(True, None, None)


def make_enquiry(intent_request):
    name = intent_request['currentIntent']['slots']['Name']
    phone = intent_request['currentIntent']['slots']['Phone']
    courses = intent_request['currentIntent']['slots']['CourseName']
    source = intent_request['invocationSource']
    output_session_attributes = intent_request['sessionAttributes'] if intent_request[
                                                                           'sessionAttributes'] is not None else {}
    # booking_map = json.loads(try_ex(lambda: output_session_attributes['bookingMap']) or '{}')
    # perform validations
    if source == 'DialogCodeHook':
        slots = intent_request['currentIntent']['slots']
        validation_result = validate_course_enquiry(name, phone, courses)
        if not validation_result['isValid']:
            slots[validation_result['violatedSlot']] = None
            return elicit_slot(
                output_session_attributes,
                intent_request['currentIntent']['name'],
                slots,
                validation_result['violatedSlot'],
                validation_result['message'],
                None
            )
        return delegate(output_session_attributes, slots)

    return close(
        output_session_attributes,
        'Fulfilled',
        {
            'contentType': 'PlainText',
            'content': 'Thanks {}, I have enrolled your for the course {}. We will see you soon'.format(name,courses)
        }

    )


def dispatch(intent_request):
    intent_name = intent_request['currentIntent']['name']
    # Dispatch to your bot's intent handlers
    if intent_name == 'CourseEnquiry':
        return make_enquiry(intent_request)
    raise Exception('Intent with name ' + intent_name + ' not supported')


def lambda_handler(event, context):
    logger.debug(event)
    return dispatch(event)

import json
from faker import Faker

def handler(event, context):
    fake = Faker()
    message = 'hello {}!'.format(fake.name())
    info = {
        "Type": "Zip Package",
        "Version": 1,
    }
    info_json = json.dumps(info)
    print(info_json)
    return {
        'message' : message
    }
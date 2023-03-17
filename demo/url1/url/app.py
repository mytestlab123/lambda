import json

def lambda_handler(event, context):
    event = json.dumps(event['body'])
    event = json.loads(event)
    print (event)
    print ("===============")
    # print (json.loads(event))
    key1 = event['key1']
    print (key1)
    return {
        "isBase64Encoded": "false",
        "statusCode": 200,
        "body": event,
        "headers": {
            "content-type": "application/json"
        }
    }
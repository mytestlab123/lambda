import json

def lambda_handler(event, context):
    print (event.keys())
    print ("===============")
    print (json.dumps(event))
    print ("===============")
    print (event)
    # body = json.loads(event['body'])
    # body = json.loads(event)
    return {
        "isBase64Encoded": "false",
        "statusCode": 200,
        "body": json.dumps(event),
        "headers": {
            "content-type": "application/json"
        }
    }
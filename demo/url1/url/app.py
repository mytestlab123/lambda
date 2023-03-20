import json

def lambda_handler(event, context):
    org = event
    # print (list(event.keys())[0])
    # print (list(event.keys())[1])
    # print (list(event.keys())[2])

    print (event.keys())
    print (event.values())
    event_dict = json.loads(event['body'])
    print (event_dict)
    print (event_dict['key1'])
    print (event_dict['key2'])
    print (event_dict['key3'])
    print (event_dict['key4'])
    
    print ("===============")
    print (event['body'])
    # exit (0)

    print (json.dumps(event))
    print (json.dumps(event['body']))
    print ("===============")
    # print (json.dumps(event['body'])['key1'])
    # print ("===============")
    # print (json.loads(event['body'])['key2'])
    # print ("===============")
    # # key1 = json.loads(event['body'])['key1']
    # print (json.loads(event['body']))
    # # print ((event['body'])['key1'])
    # print ("===============")
    # print (json.loads(event['body'])['key1'])
    # key1 = json.loads(event['body']['key1'])
    # print (key1)
    # key2 = json.dumps(event['body'])['key2']
    # print (key2)
    # event = json.dumps(event['body'])
    # event = json.loads(event)
    # print (event)
    # print ("===============")
    # # print (json.loads(event))
    # key1 = event['key1']
    # print (key1)
    return {
        "isBase64Encoded": "false",
        "statusCode": 200,
        "body": json.dumps(org),
        "headers": {
            "content-type": "application/json"
        }
    }
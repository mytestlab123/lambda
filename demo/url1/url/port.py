import json


def main():
    with open('event.json', 'r') as f:
        data = json.load(f)
    print(data)
    # event = json.load(open('event.json'))
    event = data
    print("type(event) = ", type(event))
    print (list(event.keys())[2])
    print (list(event.keys())[3])
    print (list(event.values())[3])
    chain = list(event.values())[3]
    print (chain)
    
    print (data['key4']['chain'])
    print (data['key4']['list'])
    print (len (data['key4']['list']))
    # print (data.items())
    for i in data['key4']['list']:
        print (i)
    exit (0)
    print (event.keys())
    print (event.values())
    event_dict = json.loads(event)
    print (event_dict)
    print (event_dict['key2'])
    print (event_dict['key3'])
    print (event_dict['key4'])
    
    print ("===============")


if __name__ == "__main__":
    main()
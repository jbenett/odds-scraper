import json
import datetime

with open('blob.json') as json_file:
    data = json.load(json_file)

    events = data[0]["events"]

    for e in events:
        print('Description: ' + e['description'])
        print('Start Time: ' + str(datetime.datetime.fromtimestamp(e['startTime'] / 1e3)))
        markets = e['displayGroups'][0]['markets']
        formatted_json = json.dumps(markets, indent=2)
        print(formatted_json)
        print('')

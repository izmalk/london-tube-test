import json

# Opening JSON file
f = open('train-network.json')

# returns JSON object as
# a dictionary
data = json.load(f)

# Iterating through the json
# list
for record in data['stations']:
    #print(record)
    print(record['name'])
    print(record['id'])

#for i in data['lines']:
#    print(i)


# Closing file
f.close()
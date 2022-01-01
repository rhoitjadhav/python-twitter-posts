import json

with open("some_file.json") as fp:
    json_data = json.load(fp)

print(json_data)


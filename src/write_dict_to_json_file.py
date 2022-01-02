import json

my_dict = {
    1: "one",
    2: "two"
}

with open("some_file.json") as fp:
    json.dump(my_dict, fp)


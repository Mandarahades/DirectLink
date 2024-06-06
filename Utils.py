import json


def loadJSONHostLink(filename):
    with open(file=filename) as json_file:
        data = json.load(json_file)
    return data["hosts"], data["links"]


def remove_duplicates(lst):
    unique_list = []
    for item in lst:
        if item not in unique_list:
            unique_list.append(item)
    return unique_list

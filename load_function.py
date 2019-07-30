import json

class Filter:
    def __init__(self, parent_id, data):
        if parent_id is "nomenclature_filter":
            self.prefix = data["prefix_filter"]
            self.suffix = data["suffix_filter"]
            self.file = data["file_filter"]

def parse(filename, object_name: str):
    data = {}
    with open(filename, 'r') as read_file:
        data = json.load(read_file)

    ret = None
    if data[object_name]:
        ret =  Filter(object_name, data[object_name])
    return ret

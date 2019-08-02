"""Loads json like a fool"""
import json
class Filter:
    """A faux filter like class"""
    def __init__(self, parent_id, data):
        if self.get_nomenclature_filter(parent_id):
            self.parse_nomenclature(data)

    def parse_nomenclature(self, data):
        self.prefix = data["prefix_filter"]
        self.suffix = data["suffix_filter"]
        self.file = data["file_filter"]


    def get_nomenclature_filter(self, parent_id):
        """Language doesn't have a switch"""
        return parent_id == 'nomenclature_filter'


def parse(filename, object_name: str):
    data = {}
    with open(filename, 'r') as read_file:
        data = json.load(read_file)

    ret = None
    if data[object_name]:
        ret = Filter(object_name, data[object_name])
    return ret

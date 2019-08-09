import os

from typing import List
class Filewalker:
    def __init__(self, file_filter: List = None, prefix_filter: List = None, suffix_filter: List = None,):
        self.file_filter = ['.png', '.fbx', '.max']
        if file_filter:
            self.file_filter = file_filter

        self.prefix_filter = ['ngd_valid_prefix']
        if prefix_filter:
            self.prefix_filter = prefix_filter

        self.suffix_filter = ['']
        if suffix_filter:
            self.suffix_filter = suffix_filter

        print(self.suffix_filter)
        self.passing_files = []
        self.failing_files = []

    def walk(self, walkfolder : str):
        self.passing_files = []
        self.failing_files = []
        for r, d, f in os.walk(walkfolder):
            for file in f:
                if self.match_xfix(self.prefix_filter, file) and self.match_xfix(self.suffix_filter, file) and self.match_xfix(self.file_filter, file):
                    self.passing_files.append(FileHelper(file, r))
                else:
                    self.failing_files.append(FileHelper(file, r))

    def match_xfix(self, xfix,  file):
        return any(pr in file for pr in xfix)

class FileHelper:
    def __init__(self, file, path):
        self.file = file
        self.path = path

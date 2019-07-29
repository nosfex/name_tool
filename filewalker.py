
import os
class Filewalker:
    def __init__(self, walkfolder):
        self.file_filter = ['.png', '.fbx', '.max']
        self.prefix_filter = ['ngd_valid_prefix']
        self.suffix_filter = ['']
        self.passing_files = []
        self.failing_files = []
        for r, d, f in os.walk(walkfolder):
            for file in f:
                if self.match_xfix(self.prefix_filter ,file ) and self.match_xfix( self.suffix_filter, file):
                    self.passing_files.append(file)
                else:
                    self.failing_files.append(file)

    def match_xfix(self, xfix,  file):
        for pr in self.prefix_filter:
            if pr in file:
                return True
        return False

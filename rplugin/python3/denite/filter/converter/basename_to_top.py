from pathlib import Path
from os.path import split
from denite.base.filter import Base
from denite.util import path2project, path2dir

class Filter(Base):

    def __init__(self, vim):
        super().__init__(vim)
        self.name = 'converter/basename_to_top'
        self.description = 'Place the file name at the beginning.'

    def filter(self, context):
        for candidate in context['candidates']:
            candidate_dir = path2dir(candidate['action__path'])
            root_dir = path2project(self.vim, candidate_dir, '')
            dir_name, base_name = split(candidate['action__path'])
            dir_name = Path(dir_name).relative_to(root_dir)
            if base_name:
                if str(dir_name) == '.':
                    candidate['abbr'] = base_name
                else:
                    candidate['abbr'] = "{}   [{}]".format(base_name, dir_name)
        return context['candidates']

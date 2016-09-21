# -*- coding: utf-8 -*-
import os
import fnmatch
def find(path, fnexp):
    for root, dirs, files in os.walk(path):
        for filename in fnmatch.filter(files,fnexp):
            yield os.path.join(root, filename)
for filename in find(r"e:/", "edrawmax-cn_7.8*"):
    print filename
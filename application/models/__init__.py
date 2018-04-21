import glob
from os.path import abspath, dirname, basename, isfile

from ._base import db

def _camelize(s):
    return ''.join([e.capitalize() for e in s.split('_')])

directory = abspath(dirname(__file__))
full_path_modules = glob.glob(directory+"/*.py")
ms = [basename(m)[:-3] for m in full_path_modules if isfile(m)]
for m in ms:
    if m.endswith('__init__') or\
       m.endswith('_base'):
        continue
    klass_name = _camelize(m)
    exec("from .%s import %s" %(m, klass_name))

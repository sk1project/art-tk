import json
import os
import shutil
import sys

ARTTK_CFG_PATH = os.path.expanduser('~/.config/arttk2')
TK_PATH = os.path.join(ARTTK_CFG_PATH, '_arttk')
ARTTK_CFG_FILE = os.path.join(ARTTK_CFG_PATH, 'arttk.json')

ARTTK_CFG = {}


def _setup():
    if not os.path.lexists(ARTTK_CFG_PATH):
        os.makedirs(ARTTK_CFG_PATH)
    if not os.path.lexists(TK_PATH):
        os.makedirs(TK_PATH)

        # Copy Tkinter to cash
        import Tkinter
        src = os.path.dirname(Tkinter.__file__)
        src_files = os.listdir(src)
        for file_name in src_files:
            full_file_name = os.path.join(src, file_name)
            if (os.path.isfile(full_file_name)):
                shutil.copy(full_file_name, TK_PATH)

        open(os.path.join(TK_PATH, '__init__.py'), 'w').close()

    if not os.path.lexists(TK_PATH):
        fp = open(ARTTK_CFG_FILE, 'w')
        fp.write(json.dumps(ARTTK_CFG))
        fp.close()


def init(themename=''):
    pass


_setup()
init()

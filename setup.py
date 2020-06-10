# Build command:
# > python setup.py build

import os
import sys
from cx_Freeze import setup, Executable
from boomer.main import __version__, __appname__


base = None
if sys.platform == 'win32':
    base = 'Win32GUI'

options = {
    'build_exe': {
        'includes': ['atexit']
    }
}

mainfile = os.path.abspath('boomer\\main.py')

executables = [
    Executable(mainfile, base=base, targetName='boomer.exe')
]

setup(name=__appname__,
      version=__version__,
      description='Data entry software for encoders with a deadline.',
      options=options,
      executables=executables
      )

#!c:\users\administrator\pycharmprojects\httprunner_demo\venv\scripts\python.exe
# EASY-INSTALL-ENTRY-SCRIPT: 'pyhocon==0.3.51','console_scripts','pyhocon'
__requires__ = 'pyhocon==0.3.51'
import re
import sys
from pkg_resources import load_entry_point

if __name__ == '__main__':
    sys.argv[0] = re.sub(r'(-script\.pyw?|\.exe)?$', '', sys.argv[0])
    sys.exit(
        load_entry_point('pyhocon==0.3.51', 'console_scripts', 'pyhocon')()
    )

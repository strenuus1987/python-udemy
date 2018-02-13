#!g:\gdrive\python\udemy\app8_web_based_fin_graph\www\virtual\scripts\python.exe
# EASY-INSTALL-ENTRY-SCRIPT: 'bokeh==0.12.14','console_scripts','bokeh'
__requires__ = 'bokeh==0.12.14'
import re
import sys
from pkg_resources import load_entry_point

if __name__ == '__main__':
    sys.argv[0] = re.sub(r'(-script\.pyw?|\.exe)?$', '', sys.argv[0])
    sys.exit(
        load_entry_point('bokeh==0.12.14', 'console_scripts', 'bokeh')()
    )

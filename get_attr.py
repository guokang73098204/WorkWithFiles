import os
from datetime import datetime

def get_date(timestamp):
    return datetime.utcfromtimestamp(timestamp).strftime('%d %b %Y')

def get_file_attrs(fld):
    with os.scandir(fld) as dir:
        for f in dir:
            if f.is_file():
                inf = f.stat()
                print(f'modified {get_date(inf.st_mtime)} {f.name}')

get_file_attrs('C:/vmo2/SetupDoc')
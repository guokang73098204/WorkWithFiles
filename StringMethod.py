import os

def ends_with(fld, search):
    for fn in os.listdir(fld):
        if fn.endswith(search):
            print(fn)

def starts_with(fld, search):
    for fn in os.listdir(fld):
        if fn.startswith(search):
            print(fn)


# ends_with('C:/vmo2/SetupDoc', 'docx')

starts_with('C:/vmo2/SetupDoc', 'tco')
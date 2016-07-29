
def appendEndSlash(str):
    if not str.endswith('/'):
        str += '/'
    return str

def removeEndSlash(str):
    length = len(str)
    if str.endswith('/'):
        str = str[0:length-1]
    return str

def appendStartSlash(str):
    if not str.startswith('/'):
        str = '/' + str
    return str

def removeStartSlash(str):
    length = len(str)
    if str.startswith('/'):
        str = str[1:length]
    return str
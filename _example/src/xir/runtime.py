# API Refrence https://github.com/xbimer/xbimer-docs

from XiR import runtime

class Applet(object):
    def __init__(self):
        print('__init__')
        print(runtime.python)
        print(runtime.archicad)
        print(runtime.version)


    def __kill__(self):
        print('__kill__')

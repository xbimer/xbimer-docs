# API Refrence https://github.com/xbimer/xbimer-docs

import os
from XiR import isolate

class Applet(object):
    def __init__(self):
        print('__init__')
        # show applet work dir
        print(isolate.applet)
        print(os.getcwd())
        print(os.getcwdb())

        # show storage dir
        print(isolate.storage)
        print(os.getswd())

    def __kill__(self):
        print('__kill__')

    def OnContextMenuHook(self, m):
        print('OnContextMenuHook')
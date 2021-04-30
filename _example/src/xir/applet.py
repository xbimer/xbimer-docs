# API Refrence https://github.com/xbimer/xbimer-docs

from XiR import applet

class Applet(object):
    def __init__(self):
        print('__init__')
        print(applet.id)
        print(applet.name)
        print(applet.runtime)
        print(applet.version)
        print(applet.archicads)

    def __kill__(self):
        print('__kill__')

    def OnContextMenuHook(self, m):
        m.AddItem('reboot',lambda : applet.reboot())
        m.AddItem('abort',lambda : applet.abort())
# API Refrence https://github.com/xbimer/xbimer-docs

import XiR

class Applet(object):
    def __init__(self):
        print('__init__')

    def __kill__(self):
        print('__kill__')

    def OnContextMenuHook(self, m):
        m.AddItem("l11",lambda : print("l11"))
        m.AddSeparator()
        m.StartPopupMenu("l12")
        m.AddItem("l21",lambda : print("l21"))
        m.EndPopupMenu()
        m.AddItem("l13",lambda : print("l13"),False)
        m.AddItem("l14",lambda : print("l14"),True,True)
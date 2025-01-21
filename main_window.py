# -*- coding: utf-8 -*-
import maya.cmds as cmds

try:
    import maya.OpenMayaUI as omui
    from shiboken2 import wrapInstance
except:
    pass


def runInMaya():
    print(u"Hello Maya")
    pass
    
def getWindow():
    for model_panel in cmds.getPanel(typ="modelPanel"):
        callback = cmds.modelEditor(model_panel, query=True, editorChanged=True)
        if callback == "CgAbBlastPanelOptChangeCallback":
            cmds.modelEditor(model_panel, edit=True, editorChanged="")
        
    runInMaya()

####################################################################################################
if __name__ == '__main__':
    getWindow()
    pass

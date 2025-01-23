# -*- coding: utf-8 -*-
import maya.cmds as cmds
import main_ui_learn
from imp import reload
reload(main_ui_learn) #一定要reload, 不然不重开maya就不刷新

def runInMaya():
    # print(u"Hello Maya")
    main_ui_learn.show()
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

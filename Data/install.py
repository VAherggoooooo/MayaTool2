# -*- coding:utf-8 -*- 
import os

try:
    import maya.mel as mel
    import maya.cmds as cmds
    isMaya = True
except ImportError:
    isMaya = False

def onMayaDroppedPythonFile(*args, **kwargs):
    """This function is only supported since Maya 2017 Update 3"""
    pass

def _onMayaDropped():
    """Dragging and dropping this file into the scene executes the file."""
    srcPath = os.path.dirname(__file__)
    srcPath = os.path.normpath(srcPath)

    iconPath = os.path.join(srcPath,'resource', 'icons')
    iconPath = os.path.normpath(iconPath)
    if not os.path.exists(iconPath):
        raise IOError('Cannot find ' + iconPath)
    
    p1 = os.path.dirname(__file__)
    p2 = os.path.dirname(__file__) + r'/Code'
    command = '''\
import os, sys
if not os.path.exists(r'{path}'):
    raise IOError(r'The source path "{path}" does not exist!')
if r'{path}' not in sys.path:
    sys.path.insert(0, r'{path}')
    
myPath = r'{p1}'
if myPath not in sys.path:
    sys.path.append(myPath)
myPath = r'{p2}'
if myPath not in sys.path:
        sys.path.append(myPath) 

import main_window
import pymel.core as pm
for item in pm.lsUI(editors=True):
    if isinstance(item, pm.ui.ModelEditor):
        pm.modelEditor(item, edit=True, editorChanged="")
reload(main_window)
main_window.getWindow()

'''
    command = command.format(path=srcPath, p1 = p1, p2 = p2)
    shelf = mel.eval('$gShelfTopLevel=$gShelfTopLevel')
    parent = cmds.tabLayout(shelf, query=True, selectTab=True)

    cmds.shelfButton(
        command=command,
        annotation='Maya Tool',
        sourceType='Python',
        imageOverlayLabel='MyTool',
        image=os.path.join(iconPath, 'icon.png'),
        image1=os.path.join(iconPath, 'icon.png'),
        parent=parent
    )

if isMaya:
    _onMayaDropped()


# -*- coding: utf-8 -*-
import pymel as pm
import pymel.core as pmc

def show():
    windowTag = 'MayaToolWindowTag'
    
    if(pmc.window(windowTag, q=True,exists=True)):# 如果window存在
        pmc.deleteUI(windowTag)

    if(pmc.windowPref(windowTag, q=True,exists=True)):
        pmc.windowPref(windowTag,r=True)

    theWindow = pmc.window(windowTag, t='Maya Tool Window', w=300, h=500)
    pmc.showWindow()

    
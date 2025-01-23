# -*- coding: utf-8 -*-
import pymel as pm
import pymel.core as pmc

'''
一些ui参考
国内:

国外:
http://www.not-enough.org/abe/manual/maya/pymel-quick.html

'''



def show():
    windowTag = 'MayaToolWindowTag'
    
    #删除已存在的window
    if(pmc.window(windowTag, q=True,exists=True)):# 如果window存在
        pmc.deleteUI(windowTag)
    if(pmc.windowPref(windowTag, q=True,exists=True)):
        pmc.windowPref(windowTag,r=True)

    main_width = 300
    theWindow = pmc.window(windowTag, t='Maya Window', w=main_width, h=500)# 创建window
    
    #设置主layout
    main_layout = pmc.columnLayout("Main Layout")

    ########################################################################
    #1 start
    pmc.text('text1', l='text 1:')

        #1 row
    pmc.rowColumnLayout(nc=4, cw=[(1,60),(2,90),(3,60),(4,90)])

            #1 row option1
    pmc.text('option1',l='option1:')#option1
    pmc.optionMenu('option1_options')
    pmc.menuItem(l='lf_')
    pmc.menuItem(l='rf_')
    pmc.menuItem(l='cf_')

            #1 row option2
    pmc.text('option2',l='option2:')#option2
    pmc.optionMenu('option2_options')
    pmc.menuItem(l='arm')
    pmc.menuItem(l='leg')

    #1 over
    pmc.setParent(main_layout)#回到主layout
    pmc.separator('sep1', w=main_width,h=10)#添加分隔符


    ########################################################################
    #2 start
    pmc.text('text2', l='text 2:')
    pmc.radioButtonGrp('radio_type1', labelArray3=('ik', 'fk', 'ikfk'), numberOfRadioButtons=3, columnWidth3=[main_width/3, main_width/3, main_width/3], select=3)#设置3个radio按钮组, 默认选第三个
    pmc.button('button1',l='this is button 1', w=main_width)
    #2 over
    pmc.separator('sep2', w=main_width,h=10)#添加分隔符


    ########################################################################
    #3 start
    pmc.text('text3', l='text 3:')

        #3 grid
    pmc.gridLayout(nr=1,nc=5,cellWidthHeight=[main_width/5, 20])
    pmc.iconTextButton('color_btn_1', bgc=[0.1, 0.0, 0.5])
    pmc.iconTextButton('color_btn_2', bgc=[0.32, 0.9, 0.1])
    pmc.iconTextButton('color_btn_3', bgc=[0.1, 0.67, 0.5])
    pmc.iconTextButton('color_btn_4', bgc=[0.76, 0.23, 0.2])
    pmc.iconTextButton('color_btn_5', bgc=[0.16, 0.89, 0.5])

    #3 over
    pmc.setParent(main_layout)
    pmc.colorIndexSliderGrp('color_slider1',l='color slider1:', w=main_width, h=50, cw=(main_width, 20), min=0,max=30,value=7)
    pmc.separator('sep3', w=main_width,h=10)#添加分隔符

    # 其他的奇奇怪怪
    pmc.cmdScrollFieldReporter('cmd_line', w=main_width, h=120, clear=False)
    pmc.cmdShell('cmd_shell',w=main_width, h=70)



    pmc.showWindow()# 显示window

    
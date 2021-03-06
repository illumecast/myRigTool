# -----------------------------------------------------------------------------------
# Created by ken Feb 26 2016
# Modified by ken Feb 27 2016
# Copyright (c) 2016 ken. All rights reserved.
# -----------------------------------------------------------------------------------
# import modules
# -----------------------------------------------------------------------------------

import pymel.core as pm

# -----------------------------------------------------------------------------------
# import files
# -----------------------------------------------------------------------------------

import core as core

# -----------------------------------------------------------------------------------
# GUI
# -----------------------------------------------------------------------------------

def window_creation():
    window_name='MyRiggingTool v. 1.1'

    if pm.window(window_name, exists = True):
        pm.deleteUI(window_name, window = True)
    if pm.windowPref(window_name, ex=True):
        pm.windowPref(window_name, r=True)

    window_obj = pm.window(window_name, menuBar = True)
    gui_creation()
    window_obj.show()

def gui_creation():
    pm.menu(label = 'Edit')

    pm.menuItem(
    label = 'Create Shelf Button',
    command = lambda *args: core.createShelfBtn())

    form = pm.formLayout()
    t1 = pm.text('Controller Setup')
    sep1 = pm.separator( height=40, style='in' )
    t2 = pm.text('Others')

    row1 = pm.rowLayout(numberOfColumns = 3)

    b1 = pm.button(
    annotation = 'Align selected controller with selected joint.',
    label = 'Align with Joint',
    command = lambda *args: core.alignCtrlToJnt())

    b2 = pm.button(
    annotation = 'Rename selected controller as "Selected Controller Name" + "_ctrl"',
    label='Rename',
    command = lambda *args: core.renameCtrlToJnt())

    b3 = pm.button(
    annotation = 'Freeze selected components',
    label='Freeze',
    command = 'mr.freezeAll()')

    pm.formLayout(form, edit = True,
    attachForm = [
    (t1, 'top', 5),
    (t1, 'left', 60),
    (t1, 'bottom', 5),

    (row1, 'top', 5),
    (row1, 'left', 5),
    (row1, 'bottom', 5),
    (row1, 'right', 5),

    (sep1, 'top', 5),
    (sep1, 'left', 5),
    (sep1, 'bottom', 5),

    (t2, 'top', 5),
    (t2, 'left', 80),
    (t2, 'bottom', 5)
    ],

    attachControl = [
    (t1, 'bottom', 5, row1),
    (row1, 'bottom', 5, sep1),
    (sep1, 'bottom', 5, t2)
    ],

    attachNone = [
    (row1, 'top'),
    (sep1, 'top'),
    (t2, 'top')
    ]
    )

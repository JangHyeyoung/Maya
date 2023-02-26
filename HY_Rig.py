import maya.cmds as cmds
import importlib
import Locators
import Joints

#Python 3에서는 모듈로 이동
Locators = importlib.reload(Locators)
Joints = importlib.reload(Joints)

#window
cmds.window("Hy Rig")
cmds.rowColumnLayout(nc = 2)

#button
cmds.button(l = "Create Locators",w = 200, c = "Locators.createLocators()")
cmds.button(l = "Delete Locators",w = 200, c = "deleteLocators()")
cmds.button(l = "Mirror L => R", w = 200, c = "mirrorLocators()")
cmds.button(l = "Create Joints", w = 200, c = "Joints.createJoints()")
#======================================================================
cmds.separator()
cmds.separator()

Locators.createFields()

cmds.showWindow()

######################################################################
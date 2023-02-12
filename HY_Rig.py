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

def mirrorLocators():
    allLeftLocators = cmds.ls("Loc_L_*")
    leftLocators = cmds.listRelatives(*allLeftLocators,p = True,f = True)
    #listRelatives = 계층구조로 된 object의 부모와 자식 정보얻기 , f = fullpath
    allRightLocators = cmds.ls("Loc_R_*")
    rightLocators = cmds.listRelatives(*allRightLocators,p = True,f = True)
    #enumerate 내장함수 = for 루프돌리기
    for i,l in enumerate(leftLocators):
        #위치값을 알아올땐 x,y,z 때문에 2개 이상이므로 변수명 뒤에 []를 붙인다.
        #점,면의 위치,회전,스케일등의 값을 알아오는 명령어는 xform = 트랜스폼 노드의 요소(element)관련값 가져옴.
        pos = cmds.xform(l,q = True,t = True,ws = True)
        cmds.move(-pos[0],pos[1],pos[2],rightLocators[i])

def deleteLocators():
    nodes = cmds.ls("Loc_*")
    cmds.delete(nodes)
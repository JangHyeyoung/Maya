import maya.cmds as cmds

def createJoints():
    if cmds.objExists('RIG'):
        print ('RIG already exists')
    else:
        jointGRP = cmds.group(em = True,name = "RIG") 
        
        #Create Spine
        root = cmds.ls("Loc_ROOT")
        allSpines = cmds.ls("Loc_Spine*",type = "locator")
        spine = cmds.listRelatives(*allSpines,p = True,f = True)
        rootPos = cmds.xform(root,q = True,t = True, ws = True)
        rootJoint = cmds.joint(radius = 0.1,p = rootPos,name = 'RIG_ROOT')
        #스파인의 갯수가 많으니 for문 사용
        for i,s in enumerate(spine):
            pos = cmds.xform(s,q = True,t = True,ws = True)
            j = cmds.joint(radius = 0.08,p = pos,name = 'RIG_SPINE_'+str(i))
            
        createArmJoint()
        
def createArmJoint():
    L_UpperArm = cmds.ls("Loc_L_UpperArm")
    l_UpperArmPos = cmds.xform(L_UpperArm,q=True,t=True,ws=True)
    L_UpperArmJoint = cmds.joint(radius = 0.1,p = l_UpperArmPos,name = 'RIG_L_UpperArm')
    
    L_Elbow = cmds.ls("Loc_L_LowerArm")
    l_ElbowPos = cmds.xform(L_Elbow,q=True,t=True,ws=True)
    L_ElbowJoint = cmds.joint(radius = 0.1,p = l_ElbowPos,name = 'RIG_L_Elbow')
    
    L_Wrist = cmds.ls("Loc_L_Wrist")
    l_WristPos = cmds.xform(L_Wrist,q=True,t=True,ws=True)
    L_WristJoint = cmds.joint(radius = 0.1,p = l_WristPos,name = 'RIG_L_Wrist')
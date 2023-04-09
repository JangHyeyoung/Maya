import maya.cmds as cmds

def createJoints():
    if cmds.objExists('RIG'):
        print ('RIG already exists')
    else:
        jointGRP = cmds.group(em = True,name = "RIG")
        
        spineAmount = cmds.ls("Loc_Spine*",type = 'transform')
        amount = cmds.ls("Loc_L_Finger_*_0", type = 'transform')
        
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
            
        createArmJoint(len(spineAmount))
        createHead(len(spineAmount))
        
def createArmJoint(amount):
    cmds.select(deselect = True)
    cmds.select("RIG_SPINE_"+str(amount-1))
    
    L_Clavicle = cmds.joint(radius = 0.1, p = cmds.xform(cmds.ls('Loc_L_Clavicle'), q = True, t = True, ws = True), name = "RIG_L_Clavicle")
    L_UpperArmJoint = cmds.joint(radius = 0.1, p = cmds.xform(cmds.ls('Loc_L_UpperArm'), q = True, t = True, ws = True), name = "RIG_L_UpperArm")
    
    
    L_Elbow = cmds.ls("Loc_L_LowerArm")
    l_ElbowPos = cmds.xform(L_Elbow,q=True,t=True,ws=True)
    L_ElbowJoint = cmds.joint(radius = 0.1,p = l_ElbowPos,name = 'RIG_L_Elbow')
    
    L_Wrist = cmds.ls("Loc_L_Wrist")
    l_WristPos = cmds.xform(L_Wrist,q=True,t=True,ws=True)
    L_WristJoint = cmds.joint(radius = 0.1,p = l_WristPos,name = 'RIG_L_Wrist')
    
    #===================================================================================
    cmds.select(deselect = True)
    cmds.select("RIG_SPINE_"+str(amount-1))
    
    R_Clavicle = cmds.joint(radius = 0.1, p = cmds.xform(cmds.ls('Loc_R_Clavicle'), q = True, t = True, ws = True), name = "RIG_R_Clavicle")
    R_UpperArmJoint = cmds.joint(radius = 0.1, p = cmds.xform(cmds.ls('Loc_R_UpperArm'), q = True, t = True, ws = True), name = "RIG_R_UpperArm")
    
    
    R_Elbow = cmds.ls("Loc_R_LowerArm")
    r_ElbowPos = cmds.xform(R_Elbow,q=True,t=True,ws=True)
    R_ElbowJoint = cmds.joint(radius = 0.1,p = r_ElbowPos,name = 'RIG_R_Elbow')
    
    R_Wrist = cmds.ls("Loc_R_Wrist")
    r_WristPos = cmds.xform(R_Wrist,q=True,t=True,ws=True)
    R_WristJoint = cmds.joint(radius = 0.1,p = r_WristPos,name = 'RIG_R_Wrist')
    
def createHead(amount):
    cmds.select(deselect = True)
    cmds.select("RIG_SPINE_"+str(amount-1))
    
    neckJoint = cmds.joint(radius = 0.1,p = cmds.xform(cmds.ls('Loc_Neck_Start'), q = True, t = True, ws = True), name = "RIG_Neck_Start")
    cmds.joint(radius = 0.1, p = cmds.xform(cmds.ls('Loc_Neck_End'), q = True, t = True, ws = True), name = "RIG_Neck_End")
    cmds.joint(radius = 0.1, p = cmds.xform(cmds.ls('Loc_Head'), q = True, t = True, ws = True), name = "RIG_Head")
    cmds.select(deselect = True)
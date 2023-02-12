import maya.cmds as cmds

editMode = True
#window
cmds.window("Hy Rig")
cmds.rowColumnLayout(nc = 2)
#button
cmds.button(l = "Create Locators",w = 200, c = "createLocators()")
cmds.button(l = "Delete Locators",w = 200, c = "deleteLocators()")
cmds.button(l = "Mirror L => R", w = 200, c = "mirrorLocators()")
cmds.button(l = "Create Joints", w = 200, c = "createJoints()")
#======================================================================
cmds.separator()
cmds.separator()

#spine
cmds.text("Spine Count",l = "Spine Count")
spineCount = cmds.intField(minValue=-10, maxValue=10, value=4)

#Finger
cmds.text("Finger Amount",l = "Finger Amount")
fingerCount = cmds.intField(minValue = 1,maxValue = 10, value=5)

cmds.button(l = "Edit Mode", w = 200, c = "lockAll(editMode)")

cmds.showWindow()

######################################################################

def createLocators():
    if cmds.objExists("Loc_Master"):
        print ("Loc_Master already exists")
    else:
        cmds.group(em = True , name = "Loc_Master")
    root = cmds.spaceLocator(n = "Loc_ROOT")
    cmds.scale(0.1,0.1,0.1,root)
    cmds.move(0,1,0,root)
    cmds.parent(root,"Loc_Master")
    
    createSpine()

def createSpine():
    for i in range(0,cmds.intField(spineCount,query = True,value = True)):
        spine = cmds.spaceLocator(n= "Loc_Spine"+str(i))
        cmds.scale(0.1,0.1,0.1,spine)
        if i == 0:
            cmds.parent(spine,"Loc_ROOT")
        else:
            cmds.parent(spine,"Loc_Spine"+str(i-1))
        cmds.move(0,1.25 + (0.25 * i),0,spine)
        
    createArm(1)#Left
    createArm(-1)#Right
    
def createArm(side):
    
    if side == 1:
        if cmds.objExists("Loc_L_UpperArm"):
            print ("Loc_L_Arm_GRP already exists")
        else:
            #L_arm = cmds.group(em = True , name = "Loc_L_Arm_GRP")
            #cmds.parent(L_arm,"Loc_Spine"+str(cmds.intField(spineCount,query = True,value = True)-1))
            #Upper Arm
            UpperArm = cmds.spaceLocator(n= "Loc_L_UpperArm")
            cmds.scale(0.1,0.1,0.1,UpperArm)
            cmds.parent(UpperArm,"Loc_Spine"+str(cmds.intField(spineCount,query = True,value = True)-1))
            #cmds.parent(UpperArm,L_arm)
            #Lower Arm
            LowerArm = cmds.spaceLocator(n= "Loc_L_LowerArm")
            cmds.scale(0.1,0.1,0.1,LowerArm)
            cmds.parent(LowerArm,UpperArm)
            #wrist
            Wrist = cmds.spaceLocator(n= "Loc_L_Wrist")
            cmds.scale(0.1,0.1,0.1,Wrist)
            cmds.parent(Wrist,LowerArm)
            #Upper Arm move
            cmds.move(0.35*side,1+(0.25 * cmds.intField(spineCount,query = True,value = True)),0,UpperArm)
            #Lower Arm move
            cmds.move(0.6*side,1.4,-0.2,LowerArm)
            #wrist Arm move
            cmds.move(0.8*side,1,0,Wrist)
            createHand(1,Wrist)
    else:
        if cmds.objExists("Loc_R_UpperArm"):
            print ("Loc_R_Arm_GRP already exists")
        else:
            #R_arm = cmds.group(em = True , name = "Loc_R_Arm_GRP")
            #cmds.parent(R_arm,"Loc_Spine"+str(cmds.intField(spineCount,query = True,value = True)-1))
            #Upper Arm
            UpperArm = cmds.spaceLocator(n= "Loc_R_UpperArm")
            cmds.scale(0.1,0.1,0.1,UpperArm)
            cmds.parent(UpperArm,"Loc_Spine"+str(cmds.intField(spineCount,query = True,value = True)-1))
            #Lower Arm
            LowerArm = cmds.spaceLocator(n= "Loc_R_LowerArm")
            cmds.scale(0.1,0.1,0.1,LowerArm)
            cmds.parent(LowerArm,UpperArm)
            #wrist
            Wrist = cmds.spaceLocator(n= "Loc_R_Wrist")
            cmds.scale(0.1,0.1,0.1,Wrist)
            cmds.parent(Wrist,LowerArm)
            #Upper Arm move
            cmds.move(0.35*side,1+(0.25 * cmds.intField(spineCount,query = True,value = True)),0,UpperArm)
            #Lower Arm move
            cmds.move(0.6*side,1.4,-0.2,LowerArm)
            #wrist Arm move
            cmds.move(0.8*side,1,0,Wrist)
            createHand(-1,Wrist)
            lockAll()

def createHand(side,wrist):
    if side == 1:
        if cmds.objExists("Loc_L_Hand_GRP"):
            print ("Loc_L_Hand_GRP already exists")
        else:
            hand = cmds.group(em = True , name = "Loc_L_Hand_GRP")
            pos = cmds.xform(wrist,q = True,t = True,ws = True)
            cmds.move(pos[0],pos[1],pos[2],hand)
            cmds.parent(hand,"Loc_L_Wrist")
            
            for x in range(0,cmds.intField(fingerCount,query = True,value = True)):
                createFinger(1,pos,x)
    else:
        hand = cmds.group(em = True , name = "Loc_R_Hand_GRP")
        pos = cmds.xform(wrist,q = True,t = True,ws = True)
        cmds.move(pos[0],pos[1],pos[2],hand)
        cmds.parent(hand,"Loc_R_Wrist")
        
        for x in range(0,cmds.intField(fingerCount,query = True,value = True)):
            createFinger(-1,pos,x)
            
def createFinger(side,handPos,count):
    for x in range(0,3):
        if side == 1:
            finger = cmds.spaceLocator(n = 'Loc_L_Finger_' + str(count+1) + '_' + str(x))
            cmds.scale(0.05, 0.05, 0.05, finger)
            if x == 0:
                cmds.parent(finger, 'Loc_L_Wrist')
            else:
                cmds.parent(finger, 'Loc_L_Finger_' + str(count+1) + '_' + str(x - 1))    
            cmds.move(handPos[0] + (0.1 + (0.1 * x)) * side, handPos[1] - (0.1 + (0.1 *x)), handPos[2] + -(0.05 * count), finger)
        else:        
            finger = cmds.spaceLocator(n = 'Loc_R_Finger_' + str(count+1) + '_' + str(x))
            cmds.scale(0.05, 0.05, 0.05, finger)
            if x == 0:
                cmds.parent(finger, 'Loc_R_Wrist')
            else:
                cmds.parent(finger, 'Loc_R_Finger_' + str(count+1) + '_' + str(x - 1))
            cmds.move(handPos[0] + (0.1 + (0.1 * x)) * side, handPos[1] - (0.1 + (0.1 *x)), handPos[2] + -(0.05 * count), finger)

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
            
        #Create Arm
        L_UpperArm = cmds.ls("Loc_L_UpperArm")
        l_UpperArmPos = cmds.xform(L_UpperArm,q=True,t=True,ws=True)
        L_UpperArmJoint = cmds.joint(radius = 0.1,p = l_UpperArmPos,name = 'RIG_L_UpperArm')
        
        L_Elbow = cmds.ls("Loc_L_LowerArm")
        l_ElbowPos = cmds.xform(L_Elbow,q=True,t=True,ws=True)
        L_ElbowJoint = cmds.joint(radius = 0.1,p = l_ElbowPos,name = 'RIG_L_Elbow')
        
        L_Wrist = cmds.ls("Loc_L_Wrist")
        l_WristPos = cmds.xform(L_Wrist,q=True,t=True,ws=True)
        L_WristJoint = cmds.joint(radius = 0.1,p = l_WristPos,name = 'RIG_L_Wrist')
        
        
        
        
        
def lockAll(lock):
    global editMode
    axis = ['x','y','z']
    attr = ['t','r','s']
    nodes = cmds.listRelatives("Loc_*",allParents = True)
    
    for axe in axis:
        for att in attr:
            for node in nodes:
                cmds.setAttr(node+"."+att+axe, lock = lock )
                
    if editMode == False:
        editMode = True
    else:
        editMode = False
        
def deleteLocators():
    nodes = cmds.ls("Loc_*")
    cmds.delete(nodes)
import maya.cmds as cmds

def createFields():
    global spineCount
    global fingerCount
    
    #spine
    cmds.text("Spine Count",l = "Spine Count")
    spineCount = cmds.intField(minValue=-10, maxValue=10, value=4)

    #Finger
    cmds.text("Finger Amount",l = "Finger Amount")
    fingerCount = cmds.intField(minValue = 1,maxValue = 10, value=5)
    
    cmds.button(l = "Edit Mode", w = 200, c = "lockAll(editMode)")

def createLocators():
    if cmds.objExists("Loc_Master"):
        print ("Loc_Master already exists")
    else:
        cmds.group(em = True , name = "Loc_Master")
    root = cmds.spaceLocator(n = "Loc_ROOT")
    cmds.scale(0.1,0.1,0.1,root)
    cmds.move(0,1.5,0,root)
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
        cmds.move(0,1.5 + (0.25 * i),0,spine)
    
    createHead()
    createArm(1)#Left
    createArm(-1)#Right
    createLegs(1)#Left
    createLegs(-1)#Right
    setColors()
    

def createHead():
    neck = cmds.spaceLocator(n = 'Loc_Neck_Start')
    cmds.parent(neck,'Loc_Spine' + str(cmds.intField(spineCount,query = True,value = True) - 1))
    cmds.scale(1,1, 1, neck)
    cmds.move(0,1.6 + (0.25 * 2), 0, neck) 
    
    neck = cmds.spaceLocator(n = 'Loc_Neck_End')
    cmds.parent(neck, 'Loc_Neck_Start')
    cmds.scale(1,1, 1, neck)
    cmds.move(0,1.75 + (0.25 * 2), 0, neck) 
    
    head = cmds.spaceLocator(n = 'Loc_Head')
    cmds.parent(head, 'Loc_Neck_End')
    cmds.scale(1,1,1, head)
    cmds.move(0,2+(0.25 * 2),0, head)
    
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
            
def createLegs(side):
    if side == 1:
        #Left Leg
        if cmds.objExists('L_Leg_GRP'):
            print ("L_Leg_GRP already exists")
        else:
            upperLegGRP = cmds.group(em = True, name = 'L_Leg_GRP')
            cmds.parent(upperLegGRP,'Loc_ROOT')
            cmds.move(0.1,1,0,upperLegGRP)
        
        upperLeg = cmds.spaceLocator(n = 'Loc_L_UpperLeg')
        cmds.scale(0.1,0.1,0.1, upperLeg)
        cmds.move(0.15, 1.5, 0, upperLeg)
        cmds.parent(upperLeg, 'L_Leg_GRP')
        
        ## lower leg
        lowerLeg = cmds.spaceLocator(n = 'Loc_L_LowerLeg')
        cmds.scale(0.1,0.1,0.1, lowerLeg)
        cmds.move(0.15,0.75, 0.05, lowerLeg)
        cmds.parent(lowerLeg, 'Loc_L_UpperLeg')
        
        ## foot
        foot = cmds.spaceLocator(n = 'Loc_L_Foot')
        cmds.scale(0.1, 0.1, 0.1, foot)
        cmds.move(0.15, 0.2, 0, foot)
        cmds.parent(foot, 'Loc_L_LowerLeg')
        
        ## football
        
        football = cmds.spaceLocator(n = 'Loc_L_FootBall')
        cmds.scale(0.1,0.1,0.1, football)
        cmds.move(0.15, 0, 0.15, football)
        cmds.parent(football, 'Loc_L_Foot')
        
        ## toes
        
        toes = cmds.spaceLocator(n = 'Loc_L_Toes')
        cmds.scale(0.1,0.1,0.1, toes)
        cmds.move(0.15, 0, 0.3, toes)
        cmds.parent(toes, 'Loc_L_FootBall')
        
    else:
        #Right
        if cmds.objExists('R_Leg_GRP'):
            print ("R_Leg_GRP already exists")
        else:
            upperLegGRP = cmds.group(em = True, name = 'R_Leg_GRP')
            cmds.parent(upperLegGRP,'Loc_ROOT')
            cmds.move(-0.1,1,0,upperLegGRP)
        
        upperLeg = cmds.spaceLocator(n = 'Loc_R_UpperLeg')
        cmds.scale(0.1,0.1,0.1, upperLeg)
        cmds.move(-0.15, 1.5, 0, upperLeg)
        cmds.parent(upperLeg, 'R_Leg_GRP')
        
        ## lower leg
        lowerLeg = cmds.spaceLocator(n = 'Loc_R_LowerLeg')
        cmds.scale(0.1,0.1,0.1, lowerLeg)
        cmds.move(-0.15,0.75, 0.05, lowerLeg)
        cmds.parent(lowerLeg, 'Loc_R_UpperLeg')
        
        ## foot
        foot = cmds.spaceLocator(n = 'Loc_R_Foot')
        cmds.scale(0.1, 0.1, 0.1, foot)
        cmds.move(-0.15, 0.2, 0, foot)
        cmds.parent(foot, 'Loc_R_LowerLeg')
        
        ## football
        
        football = cmds.spaceLocator(n = 'Loc_R_FootBall')
        cmds.scale(0.1,0.1,0.1, football)
        cmds.move(-0.15, 0, 0.15, football)
        cmds.parent(football, 'Loc_R_Foot')
        
        ## toes
        
        toes = cmds.spaceLocator(n = 'Loc_R_Toes')
        cmds.scale(0.1,0.1,0.1, toes)
        cmds.move(-0.15, 0, 0.3, toes)
        cmds.parent(toes, 'Loc_R_FootBall')
        
def setColors():
    cmds.setAttr('Loc_Master.overrideEnabled', 1)
    cmds.setAttr('Loc_Master.overrideRGBColors', 1)
    
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
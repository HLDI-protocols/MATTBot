from HLEngine import HLEngine_AdvancedImageProcessing
from Seeker import targetNames
filter="Filters/face.xml"
user1=targetNames.targetName[0]
user2=targetNames.targetName[1]
user3=targetNames.targetName[2]
user4=targetNames.targetName[3]
user5=targetNames.targetName[4]
user6=targetNames.targetName[5]
user7=targetNames.targetName[6]
user8=targetNames.targetName[7]
user9=targetNames.targetName[8]
user10=targetNames.targetName[9]

def lock_Target():
    HLEngine_AdvancedImageProcessing.lockTarget_Camera(filter,0,user1,user2,user3,user4,user5,user6,user7,user8,user9,user10)


lock_Target()
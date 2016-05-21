# todo: make like here https://gist.githubusercontent.com/a1ip/eb7939872dc85b5ddc2f/raw/ddeb26fbdb2885963c72d44a01742851342fc6a9/26.1-lost-viking.js

#

#
sideSteps = 1

#
steps = 1

#
X_PACE_LENGTH = 4

#
Y_PACE_LENGTH = 6
SWITCH = 5
SLIDE = 9
SKIP = 7
sidemove = 1
#
while steps <= 35:

    self.moveXY(steps * X_PACE_LENGTH, sideSteps * Y_PACE_LENGTH)
    if(steps % SWITCH == 0):
           sidemove *= -1
    if(steps % SKIP== 0):
            sideSteps += sidemove
    sideSteps += sidemove
    if(sideSteps>SLIDE):
        sideSteps = 1
    if(sideSteps<1):        
        sideSteps = SLIDE

    steps += 1    

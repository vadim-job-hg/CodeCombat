# todo: also stole

# http://codecombat.com/play/level/match-cord

fieldMap = self.findFriends()[0].getMap()
YSize = len(fieldMap)
XMiddle = 14
yes = {'x': (XMiddle - 1), 'y': (YSize - 1)}
mine = "x"
empty = "."
resultColumn = 1
mineDistance = 5
firstXPos = 15
firstYPos = 40

# Find which starting mine connects to the ogre Chieftain.


# resultColumn = 1 # fast way to win!!!!!!:-D
self.say("I think it's column number: " + resultColumn)
self.moveXY(resultColumn * mineDistance + firstXPos, firstYPos)

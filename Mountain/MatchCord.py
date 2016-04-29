#http://codecombat.com/play/level/match-cord
# Ogres mined the field to protect their Chieftain.
# But we can use the "domino" effect get our target.
# The scout has prepared the map of the minefield.
# All mines are placed the same distance apart.
# The map is an array of strings, where "x" is a mine and "." is nothing.
# The first row in the array is the row nearest to the hero.
# The map and helpful constants are listed below.
def NotInArr(what, where):
    for item in where:
        if item.x == what.x and item.y == what.y:
            return False
    return True

def checkItem(x):
    array = []
    array.push({'x':x, 'y':0, 'checked':0})
    for k in range(0, 100):
        for j in range(0, len(array)):
            if(array[j].checked==0):
                array[j].checked = 1
                check_arr = [{'x':array[j].x, 'y':array[j].y+1, 'checked':0},{'x':array[j].x+1, 'y':array[j].y, 'checked':0},{'x':array[j].x, 'y':array[j].y-1, 'checked':0},{'x':array[j].x-1, 'y':array[j].y, 'checked':0}]
                for check in check_arr:
                    if check.x>1 and check.y>1:
                        if(check.x==13 and check.y==YSize-1):
                            return True
                        elif fieldMap[check.y].substr(check.x, 1)==mine and NotInArr(check,check_arr):
                            array.push(check)
    return False

fieldMap = self.findFriends()[0].getMap()
YSize = len(fieldMap)
XMiddle = 14
yes = {'x':(XMiddle-1),'y':(YSize-1)}
mine = "x"
empty = "."
resultColumn = 1
for x in range(0, len(fieldMap[0]), 1):
    item = fieldMap[0].substr(x, 1)
    if item==mine and checkItem(x):
        resultColumn = x
mineDistance = 5
firstXPos = 15
firstYPos = 40

# Find which starting mine connects to the ogre Chieftain.


#resultColumn = 1 # fast way to win!!!!!!:-D
self.say("I think it's column number: " + resultColumn)
self.moveXY(resultColumn * mineDistance + firstXPos, firstYPos)

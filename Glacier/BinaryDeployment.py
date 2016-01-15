# http://codecombat.com/play/level/binary-deployment
def getNum(number, delimer = 2):
    return number%delimer
    
summonTypes = ['soldier', 'archer', 'griffin-rider']
def summonTroops(num, coorX, coorY):
    type = summonTypes[num]
    if self.gold > self.costOf(type):
        self.summon(type)
        friends = self.findByType(summonTypes[num], self.findFriends())
        self.command(friends[len(friends)-1], 'move', {'x':coorX, 'y':coorY})
array = [[161, 2], [96, 2], [122, 2], [120, 2], [245, 2], [724, 3], [1405, 3]]
maxY = 57
minY = 10
countY =7
minX = 20
maxX = 65
countX = 8
iY = 0
for y in range(maxY, minY-1, (minY - maxY)/(countY-1)):
    iX = 0
    number = array[iY][0]
    for x in range(maxX, minX, (minX - maxX)/countX):
        num = getNum(number, array[iY][1])
        number = Math.floor(number/array[iY][1])    
        summonTroops(num, x, y)         
        iX = iX + 1
    iY = iY + 1

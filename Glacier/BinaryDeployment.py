# http://codecombat.com/play/level/binary-deployment
# Recruit soldiers and archers to fill out each squadron.
# Each paladin has a decimal number stored in her deployment attribute.
# Convert these to binary and represent them with line soldiers and archers next to each paladin.
# Soldiers are 0s, archers are 1s.
# For the bonus goal, add griffins as 2s for trinary number lines next to the warlocks.
# Check the guide for help with binary numbers.
def getNum(number, delimer = 2):
    return number%delimer
    
summonTypes = ['soldier', 'archer', 'griffin-rider']
def summonTroops(num, coorX, coorY):
    type = summonTypes[num]
    if self.gold > self.costOf(type):
        self.summon(type)
        friends = self.findByType(summonTypes[num], self.findFriends())
        self.command(friends[len(friends)-1], 'move', {'x':coorX, 'y':coorY})
array = []
maxY = 55
minY = 10
countY =7
minX = 22
maxX = 63
countX = 8
iY = 0
friends = self.findByType('paladin', self.findFriends())
for index, friend in enumerate(friends):
       array.append([friend.deployment, 2, friend.pos.y])
friends = self.findByType('warlock', self.findFriends())
for index, friend in enumerate(friends):
       array.append([friend.deployment, 3, friend.pos.y])
for y in range(maxY, minY-1, (minY - maxY)/(countY-1)):
    iX = 0
    number = array[iY][0]
    for x in range(maxX, minX-1, (minX - maxX)/(countX-1)):
        num = getNum(number, array[iY][1])
        number = Math.floor(number/array[iY][1])    
        summonTroops(num, x, array[iY][2])         
        iX = iX + 1
    iY = iY + 1


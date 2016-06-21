#https://codecombat.com/play/level/golden-choice
# You must collect the required amount of gold.
# The gate keeper will tell you how much you need.
# Always move in the direction of the exit.
# For each row you can take only one coin.
# Choose only one from the nearest coins in the next row.

# Distance between rows and coins.
distanceX = 4
distanceY = 6
zeroPoint = {"x": 14, "y": 14}
coinLines = 10
needCollect = 74
def makeGoldMap(coins):
    template = [[0 for j in range(2 * coinLines - 1)] for i in range(coinLines)]
    for coin in coins:
        row = int((coin.pos.y - zeroPoint.y) / distanceY)
        col = int((coin.pos.x - zeroPoint.x) / distanceX)
        template[row][col] = coin.value
    return template
def getNum(number, delimer = 2):
    return number%delimer
    
# Prepare the gold map. It looks like:
# [[1, 0, 9, 0, 4],
#  [0, 1, 0, 9, 0],
#  [8, 0, 2, 0, 9]]
goldMap = makeGoldMap(hero.findItems())
for routeIndex in range(0, 100):
    number = routeIndex
    route = []
    gold = 0
    k = 9
    for y in range(0, 10):
        num = getNum(number, 2)
        number = Math.floor(number/2)
        if num==0 and k>1:#left
            gold = gold + goldMap[y][k]
            k = k - 1            
        else:#right
            k = k + 1
            gold = gold + goldMap[y][k]
    #hero.say(gold)
    if gold == needCollect:
        number = routeIndex
        break
    #break
# Find your path.
k = 9
for y in range(0, 11):
    num = getNum(number, 2)
    number = Math.floor(number/2)
    if num==0:#left
        k = k - 1            
    else:#right
        k = k + 1
    moveTo = {'x':zeroPoint.x+k*distanceX, 'y':zeroPoint.y+y*distanceY-distanceY}
    hero.moveXY(moveTo.x, moveTo.y)
    

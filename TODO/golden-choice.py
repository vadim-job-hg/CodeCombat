# Вы должны собрать требуемое количество золота.
# Хранитель врат скажет вам сколько вам нужно.
# Всё время двигаетесь в направлении выхода.
# В каждом ряды вы можете взять лишь одну монету.
# Выберите только одну из ближайших монет в слудующем ряду.

# Дистанция между рядами и монетками.
distanceX = 4
distanceY = 6
zeroPoint = {"x": 14, "y": 14}
coinLines = 10

def makeGoldMap(coins):
    template = [[0 for j in range(2 * coinLines - 1)] for i in range(coinLines)]
    for coin in coins:
        row = int((coin.pos.y - zeroPoint.y) / distanceY)
        col = int((coin.pos.x - zeroPoint.x) / distanceX)
        template[row][col] = coin.value
    return template

def getAllRotes(y, x):
    if y>9:
        return [9, 9]
    else:
        tempLeft = getAllRotes(y +1, x - 1)
        tempRight = getAllRotes(y + 1, x + 1)

goldMap = makeGoldMap(hero.findItems())
for k in range(1, 19, 2):
    allRoutes = getAllRotes()








for y in range(0, 10):
    getMax()
    if goldMap[y][k-1]>goldMap[y][k+1]:#left
        k = k - 1            
    else:#right
        k = k + 1
    moveTo = {'x':zeroPoint.x+k*distanceX, 'y':zeroPoint.y+y*distanceY}
    hero.moveXY(moveTo.x, moveTo.y)
hero.moveXY(50, 80)


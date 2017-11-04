summonTypes = {"a": "archer", "s": "soldier", "p": "peasant", "g": "griffin-rider", "P": "paladin", "A": "artillery"}
def summonTroops(num, coorX, coorY):
    type = summonTypes[num]
    if type != 'artillery' and hero.gold > hero.costOf(type):
        hero.summon(type)
    friends = hero.findByType(summonTypes[num], hero.findFriends())
    hero.command(friends[len(friends) - 1], 'move', {'x': int(coorX), 'y': int(coorY)})

sign = hero.findByType("sign")[0]
message = sign.message
for index in range(0, len(message), 5):
    type = message.substr(index, 1)
    x = message.substr(index + 1, 2)
    y = message.substr(index + 3, 2)
    summonTroops(type, x, y)

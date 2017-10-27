# https://codecombat.com/play/level/serpent-savings
def onSpawn(event):
    global coors
    while True:        
        if friend:            
            if friend.distanceTo(Vector(coors[0], coors[1]))<40:
                pet.moveXY(coorsn[0], coorsn[1])
            else:
                pet.moveXY(coors[0], coors[1])
            pet.moveXY(friend.pos.x, friend.pos.y)
        
coors =  [60, 60]
coorsn = [60, 60]
friends = hero.findFriends()
friend = friends[0]
pet.on("spawn", onSpawn)
path = [
    [70, 57],#right top
    #[72, 45],
    #[14, 45],
    #[14, 21],
    #[70, 21],
    [70, 11],#right bottom
    [7, 8],#left bottom
    [7, 57]#left Top
]
index = 0
while True:    
    friends = hero.findFriends()
    friend = friends[0]
    coors = path[index%len(path)]
    coorsn = path[(index+1)%len(path)]
    item = friend.findNearestItem()    
    if item and friend.distanceTo(item.pos)<10:
        moveto = item.pos
    else:
        moveto = Vector(coors[0], coors[1])
    enemies = friend.findEnemies()
    for enemy in enemies:
        if friend.distanceTo(enemy) < 5:
            vectorToH = Vector.subtract(friend.pos, enemy.pos)
            vectorToH = Vector.normalize(vectorToH)
            vectorToH = Vector.multiply(vectorToH, 5)
            moveto = Vector.add(vectorToH, moveto)
    hero.command(friend, "move", moveto)
    if friend.distanceTo(Vector(coors[0], coors[1]))<5:
        index+=1
    if hero.canCast('haste', friend):
        hero.cast('haste', friend)

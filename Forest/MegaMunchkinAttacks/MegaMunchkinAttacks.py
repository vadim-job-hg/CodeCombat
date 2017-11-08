path = [{'x':19,'y':33}, {'x':19,'y':14}, {'x':42,'y':14}, {'x':53,'y':37},{'x':52,'y':52}]
index = len(path)
max = len(path)
while True:
    # Найдите лучника.
    friend = hero.findNearest(hero.findFriends())
    enemy = hero.findNearestEnemy()
    
    # Прикажите лучнику атаковать противника.
    if friend and enemy:
        if(friend.distanceTo(enemy)>16):
            hero.command(friend, "attack", enemy)
        else:
            hero.command(friend, "move", path[index%len(path)])
    if(friend.pos.x == path[index % max].x):
           index = index + 1
    # Подождите-ка! Как то не очень получается. Может быть следует попробовать что-нибудь другое?
    # Манчкин ужасно меееедленный...
    
    


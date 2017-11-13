defeated = 0
while True:
    enemy = hero.findNearestEnemy()
    if enemy:
        hero.attack(enemy)
        if enemy.health <= 0:
            defeated += 1
    if hero.time > 15:
        break

hero.moveXY(59, 33)
hero.say(defeated)
gold = 0
while True:
    item = hero.findNearestItem()
    if(item):
        hero.moveXY(item.pos.x, item.pos.y)
    if hero.time > 30:
        break

hero.say(hero.gold)
defeated = 0
while True:
    enemy = hero.findNearestEnemy()
    if enemy:
        hero.attack(enemy)
        if enemy.health <= 0:
            defeated += 1
    if hero.time > 45:
        break
hero.moveXY(59, 33)
hero.say(defeated)

# http://codecombat.com/play/level/forest-pincer
# Defeat the ogres and live to cross the forest!
# Combine what you've learned about flags with your hero's combat skills.

while True:
    enemy = hero.findNearestEnemy()
    flag = hero.findFlag()
    if flag:
        hero.pickUpFlag(flag)
    elif enemy:
        if hero.isReady("cleave"):
            hero.cleave(enemy)
        else:
            hero.attack(enemy)

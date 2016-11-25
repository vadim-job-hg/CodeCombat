while True:
    enemy = hero.findNearestEnemy()
    if (enemy.type == "burl"):
        hero.say("I'm not attacking that Burl!")
    if ((enemy.type == "munchkin") or (enemy.type == "thrower")):
        hero.attack(enemy)
    if (enemy.type == "ogre"):
        hero.moveXY(43, 49)

while True:
    flag = hero.findFlag()
    enemy = hero.findNearestEnemy()
    if flag:
        hero.say("I see a flag")
    elif enemy:
        hero.attack(enemy)
    else:
        hero.say("No enemies or flags in sight.")

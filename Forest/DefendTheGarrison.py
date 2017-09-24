# https://codecombat.com/play/level/defend-the-garrison
# Победи всех атакующих огров.
# Используй флаги, чтобы держаться подальше от опасных огров.

while True:
    flag = hero.findFlag()
    enemy = hero.findNearestEnemy()
    if flag:
        # Подберите флаг.
        hero.pickUpFlag(flag)
        pass
    elif enemy:
        if (hero.isReady("cleave")):
            hero.cleave(enemy)
        elif (hero.isReady("bash")):
            hero.bash(enemy)
        elif (hero.isReady("power-up")):
            hero.powerUp()
            hero.attack(enemy)
        else:
            hero.attack(enemy)

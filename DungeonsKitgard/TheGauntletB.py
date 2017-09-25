# https://codecombat.com/play/level/the-gauntlet-b
# Используйте то, что вы изучили, чтобы победить огров.
# Помни: чтобы сокрушить огра-манчкина нужно атаковать его дважды!
while True:
    enemy = hero.findNearestEnemy()
    if enemy:
        hero.attack(enemy)
        hero.attack(enemy)
    hero.moveUp()

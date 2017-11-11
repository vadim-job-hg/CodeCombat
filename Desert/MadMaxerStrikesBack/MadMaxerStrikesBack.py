# http://codecombat.com/play/level/mad-maxer-strikes-back
# Здесь самые мелкие огры представляют наибольшую опасность!
# Сначала атакуй огров с наименьшим здоровьем.
while True:
    weakest = None
    leastHealth = 99999
    enemyIndex = 0
    enemies = hero.findEnemies()

    # Просмотрите всех врагов.
    while enemyIndex < len(enemies):
        if (enemies[enemyIndex].health < leastHealth):
            leastHealth = enemies[enemyIndex].health
            weakest = enemies[enemyIndex]
        enemyIndex = enemyIndex + 1
    # Если здоровье врага меньше чем leastHealth,

    # назначьте его слабейшим, и установите значение leastHealth равным его здоровью.

    if weakest:
        # Атакуйте слабейшего огра.
        hero.attack(weakest)
        pass

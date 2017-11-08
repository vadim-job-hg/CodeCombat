# http://codecombat.com/play/level/preferential-treatment?course=56462f935afde0c6fd30fc8c&course-instance=56fc25d7263b0220002aff0e
# Сначала цикл для всех врагов

enemies = hero.findEnemies()
enemyIndex = 0
# ...но атаковать только врагов с типом 'thrower'
while enemyIndex < len(enemies):
    if enemies[enemyIndex].type == 'thrower':
        hero.attack(enemies[enemyIndex])
    enemyIndex = enemyIndex + 1
# Теперь снова цикл для всех врагов
enemies = hero.findEnemies()
enemyIndex = 0
while enemyIndex < len(enemies):
    if enemies[enemyIndex]:
        hero.attack(enemies[enemyIndex])
    enemyIndex = enemyIndex + 1
# ...и выведи каждого, кто ещё стоит.

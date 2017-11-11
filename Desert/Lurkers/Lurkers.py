# "findEnemies" возвращает список всех ваших врагов.
# Атаковать только шаманов. Не нападайте на яков!

enemies = hero.findEnemies()
enemyIndex = 0

# Заключите весь код в цикл 'While', чтобы код учитывал весь список врагов.
while enemyIndex < len(enemies):
    enemy = enemies[enemyIndex]
    if enemy.type == 'shaman':
        while enemy.health > 0:
            hero.attack(enemy)
    enemyIndex += 1
    hero.say(enemy.type)

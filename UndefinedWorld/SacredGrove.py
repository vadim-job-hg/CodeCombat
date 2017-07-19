# https://codecombat.com/play/level/sacred-grove
# Не позволь ограм вступить в рощу.

def onSpawn():
    while True:
        scout = pet.findNearestByType("scout")
        if scout and pet.isReady("charm"):
            pet.charm(scout)

# Назначь обработчик событий на событие питомца "spawn".
pet.on('spawn', onSpawn)
# Сражайся!
while True:
    enemy = hero.findNearestEnemy()
    if enemy and enemy.pos.x<20: 
        hero.attack(enemy)

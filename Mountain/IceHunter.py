#https://codecombat.com/play/level/ice-hunter
# Should fill in some default source

while True:
    enemies = hero.findEnemies()
    health = 999999
    target = None
    if len(enemies)>0:
        for enemy in enemies:
            if enemy.health<health and enemy.type=='ice-yak':
                health = enemy.health
                target = enemy
        if target:
            hero.attack(target)

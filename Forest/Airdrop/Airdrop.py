def onSpawn (event):
    while True:
        item = hero.findNearestItem()
        if item:
            pet.fetch(item)
        
pet.on("spawn", onSpawn)

while True:
    enemy = hero.findNearestEnemy()
    if enemy and enemy.pos.x<25:
        hero.attack(enemy)
    

    

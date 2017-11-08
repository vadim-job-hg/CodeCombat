# https://codecombat.com/play/level/airdrop
# Get all swords and protect the village.

def onSpawn (event):
    while True:
        item = hero.findNearestItem()
        if item:
            pet.fetch(item)
        

# Assign onSpawn function for the pet's "spawn".
pet.on("spawn", onSpawn)

while True:
    # Guard the left passage: 
    enemy = hero.findNearestEnemy()
    if enemy and enemy.pos.x<25:
        hero.attack(enemy)
    

    

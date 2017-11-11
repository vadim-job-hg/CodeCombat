# https://codecombat.com/play/level/key-traps
# Get three keys and free the paladin.

def onSpawn(event):
    # The pet should find and fetch three keys.
    # You need: "bronze-key". "silver-key" and "gold-key".
    potion = pet.findNearestByType("bronze-key")
    if potion:
        pet.fetch(potion)
    potion = pet.findNearestByType("silver-key")
    if potion:
        pet.fetch(potion)
    potion = pet.findNearestByType("gold-key")
    if potion:
        pet.fetch(potion)
    

pet.on("spawn", onSpawn)

while True:
    enemy = hero.findNearestEnemy()
    if enemy and enemy.team == "ogres":
        hero.attack(enemy)
    if hero.health < 300:
        # You can use pets in the main thread too.
        potion = pet.findNearestByType("potion")
        if potion:
            hero.moveXY(potion.pos.x, potion.pos.y)

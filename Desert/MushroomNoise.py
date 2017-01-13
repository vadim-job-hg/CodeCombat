# https://codecombat.com/play/level/mushroom-noise
# Should fill in some default source
def onSpawn (event):
    potion = pet.findNearestByType("potion")
    pet.fetch(potion)
    goldKey = pet.findNearestByType("gold-key")
    pet.fetch(goldKey)

skeleton = pet.findNearestByType("skeleton")
pet.on("spawn", onSpawn)

while True:
    if skeleton.health > 0:
        hero.attack(skeleton)
    else:
        hero.moveXY(31, 38)

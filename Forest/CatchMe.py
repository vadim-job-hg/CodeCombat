# https://codecombat.com/play/level/catch-me
# Protect the village from ogres catapults.
# Be aware of shamans and don't stand out the village.

# Write the function "hitAndRun".
# If there is a target, then hit it and run in the village.
def hitAndRun():
    enemy = hero.findNearestEnemy()
    if enemy and enemy.pos.y>20 and enemy.pos.y<30:
        hero.attack(enemy)
        hero.moveXY(44, 25)

while True:
    enemy = hero.findNearestEnemy()
    hitAndRun(enemy)

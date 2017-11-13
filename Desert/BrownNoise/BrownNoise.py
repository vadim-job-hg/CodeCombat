# https://codecombat.com/play/level/brown-noise
# Collect the treasure and escape.

# Prepare the hero and the pet.
pet.moveXY(32, 28)
hero.moveXY(10, 19)
# Distract the skeleton.
pet.distractionNoise()
enemy = hero.findNearestEnemy()
hero.backstab(enemy)
# Sneak while the skeleton is distracted.
hero.moveXY(10, 46)
hero.moveXY(49, 47)
pet.moveXY(64, 28)
hero.moveXY(49, 38)
# Repear this maneuver to get the treasure:
pet.distractionNoise()
hero.moveXY(49, 18)
hero.moveXY(49, 8)
hero.moveXY(72, 8)
hero.moveXY(49, 8)
hero.moveXY(49, 18)
pet.distractionNoise()
# Escape from the dungeon (the red mark):
hero.moveXY(49, 47)
hero.moveXY(40, 47)
hero.moveXY(40, 56)
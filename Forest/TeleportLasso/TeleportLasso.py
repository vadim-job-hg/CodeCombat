# https://codecombat.com/play/level/teleport-lasso
# Our wizards teleport ogres from their camp here.
# They appear for a short period and they are stunned.
# If you attack an ogre, it stays here and can counterattack.
# Attack only weak and near ogres.

# Our wizards teleport ogres from their camp here.
# They appear for a short period and they are stunned.
# If you attack an ogre, it stays here and can counterattack.
# Attack only weak and near ogres.

while True:
    enemy = hero.findNearestEnemy()
    if enemy:
        distance = hero.distanceTo(enemy)
    # If enemy's type is "munchkin" AND the distance to it less than 20 metres.
    if enemy and enemy.type == 'munchkin' and distance < 20:
        # Then attack it.
        hero.attack(enemy)

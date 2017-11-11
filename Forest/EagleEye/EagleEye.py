# https://codecombat.com/play/level/eagle-eye
# This baby griffin will help you spot Ogres!

while True:
    target = hero.findNearestEnemy()
    # Some of the targets will be Burls. You don't want to attack them!
    # Use this to tell if you should attack:  hero.isOgre(target)
    if target and target.type != 'burl':  # ∆ Change this!
        hero.attack(target)

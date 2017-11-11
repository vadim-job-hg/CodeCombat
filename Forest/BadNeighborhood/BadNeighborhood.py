# https://codecombat.com/play/level/bad-neighborhood
# Only attack ogres who get close to you.
while True:
    target = hero.findNearestEnemy()
    # Use this to tell if you should attack:  hero.isClose(target)
    if target and hero.distanceTo(target) < 5:  # ∆ Change this!
        hero.attack(target)

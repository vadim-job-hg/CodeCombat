# https://codecombat.com/play/level/elseweyr
# Your cleave is on a 10 second cooldown.
# Use an else-statement to defend yourself while recharging.

while True:
    enemy = hero.findNearestEnemy()
    if hero.isReady("cleave"):
        hero.cleave()
    # Write else: to do something when cleave isn't ready:
    else:
        # Be sure to attack the enemy:
        if enemy:
            hero.attack(enemy)


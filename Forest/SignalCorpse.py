# You can use flags to choose different tactics.
# In this level, the green flag will mean you want to move to the flag.
# The black flag means you want to cleave at the flag.
# The doctor will heal you at the Red X

while True:
    green = hero.findFlag("green")
    black = hero.findFlag("black")
    nearest = hero.findNearestEnemy()
    enemy = hero.findNearestEnemy()
    if enemy:
        dist = hero.distanceTo(enemy);
    if green:
        hero.pickUpFlag(green)
    elif black and hero.isReady("cleave"):
        hero.pickUpFlag(black)
        enemy = hero.findNearestEnemy()
        if enemy:
            hero.cleave(enemy);

    elif nearest and hero.distanceTo(nearest) < 10:
        hero.attack(nearest)

        pass

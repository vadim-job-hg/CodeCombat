# http://codecombat.com/play/level/the-agrippa-defense-a
def cleaveOrAttack(enemy):
    # If "cleave" is ready, cleave; otherwise, attack.
    # enemy = hero.findNearestEnemy()
    enemy = hero.findNearestEnemy()
    if (enemy):
        dist = hero.distanceTo(enemy)
        if (dist < 5):
            if (hero.isReady("cleave")):
                hero.cleave(enemy)
            else:
                hero.attack(enemy)

    pass


while True:
    enemy = hero.findNearestEnemy()
    if enemy:
        distance = hero.distanceTo(enemy)
        if distance < 5:
            # Call the "cleaveOrAttack" function, defined above.
            cleaveOrAttack(enemy)

# https://codecombat.com/play/level/picnic-buster
# Помните, что врага в данный момент может не быть рядом.
while True:
    enemy = hero.findNearestEnemy()
    # Но когда он появится, атакуйте!
    if enemy and hero.distanceTo(enemy) < 20:
        hero.attack(enemy)

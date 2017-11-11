# https://codecombat.com/play/level/patrol-buster-a
# Помните, что врага в данный момент может не быть рядом.
while True:
    enemy = hero.findNearestEnemy()
    if enemy:
        # Но когда он появится, атакуйте!
        hero.attack(enemy)
        pass

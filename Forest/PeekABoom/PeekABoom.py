# https://codecombat.com/play/level/peek-a-boom

# <%= build_traps %>

while True:
    enemy = hero.findNearestEnemy()
    if enemy:
        # <%= build_fire-trap %>
        hero.buildXY('fire-trap', 41, 24)
        hero.moveXY(19, 19)
        pass
    # <%= add_else %>
    else:
        # <%= move_wooden %>
        hero.moveXY(19, 19)

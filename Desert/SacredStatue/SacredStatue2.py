# http://codecombat.com/play/level/sacred-statue
# Прогуляйтесь вокруг позиций огров, уничтожайте каждого врага, что повстречаете на своем пути.
# Посетите статую, что бы начать бой.
NE = {"x": 50, "y": 80}
SE = {"x": 50, "y": 50}
SW = {"x": 75, "y": 50}
NW = {"x": 75, "y": 80}
hero.moveXY(60, 65)
while True:
    # Удерживайте позици и победите атакующих огров.
    enemy = hero.findNearestEnemy()
    enemies = hero.findEnemies()
    #if enemy and 15<hero.distanceTo(enemy) and hero.distanceTo(enemy)<hero.throwRange:
    #    hero.throw(enemy)
    if len(enemies)>10 and hero.isReady('wall-of-darkness') and 30<hero.distanceTo(enemy):
        hero.wallOfDarkness([NE, SE, SW, NW, NE])
    elif len(enemies)>20 and hero.isReady('shadow-vortex'):
        hero.shadowVortex(Vector(60, 55), Vector(enemy.pos.x, enemy.pos.y))
    elif enemy and hero.distanceTo(enemy)<hero.attackRang/3:
        hero.scattershot(enemy)
    elif enemy:
        hero.attack(enemy)
    else:
        hero.moveXY(60, 65)  # Подсказка: в бою держитесь рядом со статуей, она окажет поддержку во время сражения.

    # После того как вы одержите победу над ограми, вам предстоит сразиться с Древним Циклопом!

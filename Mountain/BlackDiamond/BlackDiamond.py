# https://codecombat.com/play/level/black-diamond
# use ring of speed
while True:
    gem = hero.findNearestItem()
    if gem:
        clear = hero.isPathClear(hero.pos, gem.pos)
    else:
        clear = False
    # Метод isPathClear моказывает наличие препятствий на пути.
    # Если все чисто, иди к камню. Используй move() и gem.pos.
    if clear:
        lastpos = {'x': hero.pos.x, 'y': hero.pos.y}
        hero.moveXY(gem.pos.x, gem.pos.y)
    else:
        hero.moveXY(lastpos.x, lastpos.y)
        hero.moveXY(40, 35)
    # В противном случае возвращайся в центр.

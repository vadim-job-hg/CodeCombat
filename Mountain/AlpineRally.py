# https://codecombat.com/play/level/alpine-rally
# Выход находится в правой части уровня.
# Чтобы убежать от йети, вы должны сделать себя быстрее.
# Используйте сброс усталости ('resetCooldown'), чтобы использовать заклинание или умение более часто.
# МанаВзрыв должен помочь очистить путь.
invis = -5
while True:
    if (hero.now() - invis > 4):
        if (hero.canCast('haste', self)):
            hero.cast('haste', self)
    if (hero.canCast('invisibility', self)):
        hero.cast('invisibility', self)
        invis = hero.now()
    # if(not(hero.hasEffect('invisibility')) and hero.canCast('earthskin', self)):
    #    hero.cast('earthskin', self)
    direction = Vector(hero.pos.x + 30, hero.pos.y)
    enemy = hero.findNearest(hero.findByType('scout'))
    # if(hero.canCast('chain-lightning', enemy)):
    #    hero.cast('chain-lightning', enemy)
    hero.move(direction)

#https://codecombat.com/play/level/alpine-rally
# Выход находится в правой части уровня.
# Чтобы убежать от йети, вы должны сделать себя быстрее.
# Используйте сброс усталости ('resetCooldown'), чтобы использовать заклинание или умение более часто.
# МанаВзрыв должен помочь очистить путь.
invis = -5
loop:
    if(hero.now() - invis>4):
        if(self.canCast('haste', self)):
            self.cast('haste', self)
    if(self.canCast('invisibility', self)):
        self.cast('invisibility', self)
        invis = hero.now()
    #if(not(self.hasEffect('invisibility')) and self.canCast('earthskin', self)):
    #    self.cast('earthskin', self)
    direction = Vector(hero.pos.x + 30, hero.pos.y)
    enemy = hero.findNearest(hero.findByType('scout'))
    #if(hero.canCast('chain-lightning', enemy)):
    #    hero.cast('chain-lightning', enemy)
    hero.move(direction)

while True:
    flag = hero.findFlag()
    if (flag):
        if hero.distanceTo(flag) > 10 and hero.isReady('jump'):
            hero.jumpTo(flag.pos)
        else:
            hero.pickUpFlag(flag)
    else:
        hero.shield()

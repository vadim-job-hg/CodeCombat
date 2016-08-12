# https://codecombat.com/play/level/apocalypse
# Пушка апокалипсиса направлена на нас!
# Уклоняйтесь от летящих снарядов в течении 60 секунд.
# Подсказка: флаги могут оказаться полезными.
# Поскольку атаки распределяются случайным образом, каждый раз при загрузке, Вы не сможете уклоняться используя метод moveXY()
while True:
    flag = hero.findFlag()
    if (flag):
        if hero.distanceTo(flag) > 10 and hero.isReady('jump'):
            hero.jumpTo(flag.pos)
        else:
            hero.pickUpFlag(flag)
    else:
        hero.shield()

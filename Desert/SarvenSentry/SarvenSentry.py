# Используй флаги разных цветов, чтобы выполнять различные задачи.

while True:
    flagGreen = hero.findFlag("green")
    flagBlack = hero.findFlag("black")
    flagViolet = hero.findFlag("violet")
    if (flagGreen):
        hero.buildXY('fence', flagGreen.pos.x, flagGreen.pos.y)
        hero.pickUpFlag(flagGreen)
    # Если появляется зеленый флаг, то строй заграждение ("fence").
    if (flagBlack):
        hero.buildXY('fire-trap', flagBlack.pos.x, flagBlack.pos.y)
        hero.pickUpFlag(flagBlack)
    # Если появляется черный флаг, то строй ловушку ("fire-trap").
    if (flagViolet):
        hero.moveXY(flagViolet.pos.x, flagViolet.pos.y)
        hero.pickUpFlag(flagViolet)
        # Если появляется фиолетовый флаг, то просто переместись к нему.

        # Не забывай подбирать флаги после их использования!

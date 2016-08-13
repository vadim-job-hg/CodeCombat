# Используй флаги разных цветов, чтобы выполнять различные задачи.

while True:
    flagGreen = self.findFlag("green")
    flagBlack = self.findFlag("black")
    flagViolet = self.findFlag("violet")
    if (flagGreen):
        self.buildXY('fence', flagGreen.pos.x, flagGreen.pos.y)
        self.pickUpFlag(flagGreen)
    # Если появляется зеленый флаг, то строй заграждение ("fence").
    if (flagBlack):
        self.buildXY('fire-trap', flagBlack.pos.x, flagBlack.pos.y)
        self.pickUpFlag(flagBlack)
    # Если появляется черный флаг, то строй ловушку ("fire-trap").
    if (flagViolet):
        self.moveXY(flagViolet.pos.x, flagViolet.pos.y)
        self.pickUpFlag(flagViolet)
        # Если появляется фиолетовый флаг, то просто переместись к нему.

        # Не забывай подбирать флаги после их использования!

# http://codecombat.com/play/level/lost-viking
# Вам НЕОБХОДИМО нажать на кнопку ПОМОЩЬ чтобы увидеть детальное описание уровня!

# Ворон подскажет вам какие параметры лабиринта вам нажны!

# Как много sideSteps(шагов в сторону) к северу от Красного Креста вы сделали.
sideSteps = 1

# Как много steps(шагов) к востоку от Красного Креста вы сделали.
steps = 1

# Перемножьте это с количеством шагов на восток(step), чтобы определить свою X координату. НЕ ИЗМЕНЯЙТЕ ЭТО!
X_PACE_LENGTH = 4

# Перемножьте это с количеством шагов к северу(sideSteps), чтобы определить свою Y координату. НЕ ИЗМЕНЯЙТЕ ЭТО!
Y_PACE_LENGTH = 6
SWITCH = 6
SLIDE = 8
SKIP = 11
sidemove = 1
# Лабиринт это 35 шагов вдоль Оси X.
while steps <= 35:
    # Сделайте следующий шаг:
    hero.moveXY(steps * X_PACE_LENGTH, sideSteps * Y_PACE_LENGTH)
    if (steps % SWITCH == 0):
        sidemove = sidemove * -1
    sideSteps += sidemove
    if (steps % SKIP == 0):
        sideSteps = sideSteps + sidemove
    if (sideSteps > SLIDE):
        sideSteps = sideSteps - SLIDE
    if (sideSteps < 1):
        sideSteps = sideSteps + SLIDE
        # Увеличивайте steps(шаги) и sideSteps(шаги в сторону) по необходимости, принимая во внимание специальные правила.
    steps += 1


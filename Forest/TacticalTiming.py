# https://codecombat.com/play/level/tactical-timing
# Помогите на передней линии.
# Возвращайтесь к флагу, если кто-нибудь пытается прокрасться.
while True:
    flag = hero.findFlag()
    enemy = hero.findNearestEnemy()
    if flag:
        hero.pickUpFlag(flag)
    elif enemy:
        hero.attack(enemy)


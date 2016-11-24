#https://codecombat.com/play/level/tactical-timing
# Помогите на передней линии.
# Возвращайтесь к флагу, если кто-нибудь пытается прокрасться.
while True:
    flag = self.findFlag()
    enemy = self.findNearestEnemy()
    if flag:
        self.pickUpFlag(flag)
    elif enemy:
        self.attack(enemy)


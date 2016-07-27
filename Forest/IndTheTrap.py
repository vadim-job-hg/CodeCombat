# Если ты попробуешь атаковать врага, твой герой будет это делать, игнорируя все флаги. 
# Ты должен убедиться, что ты атакуешь врагов, которые находятся рядом с тобой!

loop:
flag = self.findFlag()
enemy = self.findNearestEnemy()
if enemy:
    dist = self.distanceTo(enemy)
if flag:
    # Возьми флаг.
    self.pickUpFlag(flag)
    self.say("Я должен взять флаг.")
elif enemy:
    if (dist < 10):
        self.attack(enemy)

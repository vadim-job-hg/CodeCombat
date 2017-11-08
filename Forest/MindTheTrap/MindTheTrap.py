# Если ты попробуешь атаковать врага, твой герой будет это делать, игнорируя все флаги. 
# Ты должен убедиться, что ты атакуешь врагов, которые находятся рядом с тобой!

while True:
    flag = hero.findFlag()
    enemy = hero.findNearestEnemy()
    if enemy:
        dist = hero.distanceTo(enemy)
    if flag:
        # Возьми флаг.
        hero.pickUpFlag(flag)
        hero.say("Я должен взять флаг.")
    elif enemy:
        if (dist < 10):
            hero.attack(enemy)

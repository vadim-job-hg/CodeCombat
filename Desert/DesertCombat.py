# http://codecombat.com/play/level/desert-combat
ordersGiven = 0
while ordersGiven < 5:
    x = hero.pos.x
    y = hero.pos.y - 10
    hero.moveXY(x, y)
    # Перемещайся и отдавай приказы каждому из союзников. (Они тебя слышат только если ты стоишь напротив них.)
    hero.say("Attack!")
    ordersGiven += 1;
    if (ordersGiven >= 5):
        break;
hero.moveXY(48, 31)
while True:
    enemy = hero.findNearestEnemy()
    hero.attack(enemy)

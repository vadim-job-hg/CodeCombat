# http://codecombat.com/play/level/bombing-run
# Incoming oscars! (That's military speak for ogres).
# Тебе нужно рассчитать угол их атаки.
# Используй тригонометрию, чтобы найти угол в радианах!

while True:
    enemy = hero.findNearestEnemy()
    if enemy and hero.distanceTo(enemy) < 70:
        O = Math.abs(enemy.pos.y - hero.pos.y)
        A = Math.abs(enemy.pos.x - hero.pos.x)
        angle = Math.atan2(O, A)
        angle = angle * 180 / Math.PI
        if enemy.pos.x < hero.pos.x:
            angle = 180 - angle
        hero.say(angle)

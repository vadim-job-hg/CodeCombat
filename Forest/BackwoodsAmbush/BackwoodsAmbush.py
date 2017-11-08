# http://codecombat.com/play/level/backwoods-ambush
# Двигайтесь к каждой контрольной точке и выманивайте каждого огра.
hero.moveXY(24, 42)
enemy1 = hero.findNearestEnemy()
# Используйте оператор "if", чтобы убедиться в присутствии врага перед атакой
if enemy1:
    hero.attack(enemy1)
    hero.attack(enemy1)

hero.moveXY(27, 60)
enemy2 = hero.findNearestEnemy()
if enemy2:
    hero.attack(enemy2)
    hero.attack(enemy2)

hero.moveXY(42, 50)
# Добавте еще один оператор "if" и атакуйте.
enemy3 = hero.findNearestEnemy()
if enemy3:
    hero.attack(enemy3)
    hero.attack(enemy3)
hero.moveXY(39, 24)
# Переходите к следующим двум контрольным точкам и выманивайте оставшихся врагов.
enemy4 = hero.findNearestEnemy()
if enemy4:
    hero.attack(enemy4)
    hero.attack(enemy4)

hero.moveXY(55, 29)
# Переходите к следующим двум контрольным точкам и выманивайте оставшихся врагов.
enemy5 = hero.findNearestEnemy()
if enemy5:
    hero.attack(enemy5)
    hero.attack(enemy5)

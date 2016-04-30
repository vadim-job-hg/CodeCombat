#http://codecombat.com/play/level/destroying-angel
hero.moveDown()
hero.moveRight()
hero.moveDown()
# Мама всегда говорила: "Ешь случайные грибы, которые найдёшь в подземельях".

hero.moveDown()
hero.moveRight()
hero.moveRight()
hero.moveRight()
hero.moveUp()
hero.moveLeft()
hero.moveUp()
hero.moveRight()
hero.moveUp()
hero.moveLeft()
hero.moveDown()
# Найди свой путь к Dungeon Keeper-у.

while True:
    enemy = hero.findNearestEnemy()
    if enemy:
        hero.attack(enemy)


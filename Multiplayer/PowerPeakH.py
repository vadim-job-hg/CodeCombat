# todo:
# https://codecombat.com/play/level/power-peak?team=humans&course=56462f935afde0c6fd30fc8c&course-instance=56fc25d7263b0220002aff0e
# https://codecombat.com/play/level/power-peak?course=5632661322961295f9428638&codeLanguage=python
# Welcome to the Course 2 Arena. Defend against waves of ogres!
# Survive longer than your enemy to win!

def petLogic():
    # Add code to use your pet!
    # Move them to the power discs at the top of the map for powerups.
    while True:
        pet.moveXY(51, 74);
        item = pet.findNearestItem()
        if item:
            pet.fetch(item)


pet.on('spawn', petLogic)
while True:
    # Improve your hero's default code!
    # Move to the nearby power discs to spawn units to help or attack!

    enemy = hero.findNearestEnemy()
    item = hero.findNearestItem()
    if enemy:
        if hero.isReady('cleave'):
            hero.cleave(enemy)
        else:
            hero.attack(enemy)
    elif item:
        hero.moveXY(item.pos.x, item.pos.y)



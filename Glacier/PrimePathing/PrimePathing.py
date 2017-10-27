# Get all your troops to the end of the path by passing over the mines.
# You can locate duds by finding the mines that have a value that is a prime number.
# Check the guide for clarification.

def primeCheck(number):
    for i in range(2,(number**0.5)):
        if number % i == 0:
            return False
    return True

friends = hero.findFriends()
mines = hero.findHazards()
firstMines = []
for mine in mines:
    if mine.pos.y > 30 and mine.pos.x < 80:
        if primeCheck(mine.value):
            firstMines.append(mine)
for mine in firstMines:
    if mine.pos.x > (hero.pos.x - 25):
        hero.moveXY(mine.pos.x + 10, mine.pos.y)
        hero.moveXY(mine.pos.x, mine.pos.y)
        hero.moveXY(hero.pos.x - 10, hero.pos.y)
        for friend in friends:
            hero.command(friend, "move", {"x": mine.pos.x + 10, "y": mine.pos.y})
            hero.wait(1.6)
            hero.command(friend, "move", {"x": mine.pos.x, "y": mine.pos.y})
            hero.command(friend, "move", {"x": mine.pos.x - 10, "y": mine.pos.y})
hero.moveXY(2, 15)
for friend in friends:
    hero.command(friend, "move", {"x": 2, "y": 15})

secondMines = []
for mine in mines:
    if mine.pos.y < 30 and mine.pos.x < 80:
        if primeCheck(mine.value):
            secondMines.append(mine)
while hero.pos.x < 75:
    for mine in secondMines:
        if mine.pos.x < (hero.pos.x + 25) and mine.pos.x > hero.pos.x:
            hero.moveXY(mine.pos.x - 10, mine.pos.y)
            hero.moveXY(mine.pos.x, mine.pos.y)
            hero.moveXY(hero.pos.x + 10, hero.pos.y)
            for friend in friends:
                hero.command(friend, "move", {"x": mine.pos.x - 5, "y": mine.pos.y})
                hero.wait(1.6)
                hero.command(friend, "move", {"x": mine.pos.x, "y": mine.pos.y})
                hero.command(friend, "move", {"x": mine.pos.x + 12, "y": mine.pos.y})

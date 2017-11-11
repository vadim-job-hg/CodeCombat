# https://codecombat.com/play/level/distracting-dungeon
# Navigate the mountain maze with a peasant pal.
# Advanced while-loop usage is required!

peasant = hero.findNearest(hero.findFriends())
while hero.pos.x<96:
    # Command your friend to build a decoy towards x + 1:
    hero.command(peasant, 'buildXY', 'decoy', hero.pos.x+1, hero.pos.y)
    tDest = {"x": hero.pos.x, "y": hero.pos.y + 28};
    while hero.distanceTo(tDest) > 1:
        hero.move(tDest)
        hero.command(peasant, "move", tDest)
    # Create a new x/y object +28 units away in the x dir:
    tDest = {"x": hero.pos.x+28, "y": hero.pos.y};
    # Find the nearest enemy:
    enemy = hero.findNearestEnemy()
    # While there is an enemy:
    while enemy:
        # While the enemy's health is > 0:
        while enemy.health>0:
            # Attack the enemy:
            hero.attack(enemy)
        # Update the variable to the next nearest enemy:
        enemy = hero.findNearestEnemy()
    # While friend's distance to the new x/y object > 1:
    hero.say(peasant.distanceTo(tDest))
    while peasant.distanceTo(tDest)>1:
        # Move the hero and peasant towards the x/y dict:
        hero.command(peasant, 'move', tDest)
        hero.wait(3)

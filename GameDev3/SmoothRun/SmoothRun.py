# Animate static objects.

hero = game.spawnHeroXY("captain", 4, 34)
hero.maxSpeed = 12

# Fences will be our "enemies" here.
fence1 = game.spawnXY("fence", 10, 10)
# This property will define the moving direction: 1 is up, -1 is down.
fence1.dir = 1
fence2 = game.spawnXY("fence", 22, 56)
fence2.dir = -1
fence3 = game.spawnXY("fence", 34, 22)
fence3.dir = 1
fence4 = game.spawnXY("fence", 46, 44)
fence4.dir = -1
fence5 = game.spawnXY("fence", 58, 34)
fence5.dir = 1
fence6 = game.spawnXY("fence", 70, 34)
fence6.dir = -1

# This fire-spewer will move along the top, spewing fire.
spewer = game.spawnXY("fire-spewer", 70, 62)
spewer.direction = "vertical"
spewer.spamInterval = 9000
spewer.spamEvery = 0.4
spewer.scale = 2
# This property will define the moving direction: 1 is right, -1 is left.
spewer.dir = -1

# The speed of the fences and the spewer: meters per frame. Remember there are 30 frames per second.
fenceSpeed = 0.8
spewerSpeed = 1.2


# This function moves the spewer.
def onUpdateSpewer(event):
    spewer = event.target
    # Multiply the spewer speed by the moving direction.
    dist = spewerSpeed * spewer.dir
    # Add the result to x coordinate.
    spewer.pos.x += dist
    # If the spewer is out of the range (10, 70).
    if spewer.pos.x > 70 or spewer.pos.x < 10:
        # Then it's time to change the moving direction.
        spewer.dir *= -1


game.setActionFor("fire-spewer", "update", onUpdateSpewer)


# This function moves the fences.
def onUpdateFence(event):
    fence = event.target
    # Multiply fenceSpeed and fence.dir to calculate the moving distance and direction.
    # Assign the result to the variable 'dist':
    dist = fenceSpeed * fence.dir
    # Add the value of the 'dist' variable to fence.pos.y:
    fence.pos.y += dist
    # If the fence's y position is less than 10 or greater than 56:
    if fence.pos.y > 56 or fence.pos.y < 10:
        # Multiply fence.dir by -1 and save it:
        fence.dir *= -1


game.setActionFor("fence", "update", onUpdateFence)


# This function tracks hero collisions.
def onCollide(event):
    unit = event.target
    collided = event.other
    if collided.type == "fence" or collided.type == "fire-spewer":
        unit.defeat()


hero.on("collide", onCollide)

game.addSurviveGoal()
game.addMoveGoalXY(77, 34)

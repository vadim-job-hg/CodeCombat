# https://codecombat.com/play/level/berserker
# Use the new "collide" event to clear the path.

hero = game.spawnHeroXY('captain', 12, 34)
hero.maxSpeed = 15
game.addMoveGoalXY(76, 34)
ui.track(game, "time")

# The duration of the mushroom power.
game.powerDuration = 5
# Use it to track the power time.
game.powerEndTime = 0

# Mushroom are collectable items without default effects.
game.spawnXY("mushroom", 12, 52)
game.spawnXY("mushroom", 12, 16)
# Spawn more mushrooms.
game.spawnXY("mushroom", 36, 16)
game.spawnXY("mushroom", 36, 52)
game.spawnXY("mushroom", 56, 12)
game.spawnXY("mushroom", 56, 56)
game.spawnXY("mushroom", 56, 34)

# The event handler to act for collected mushrooms.
def onCollect(event):
    player = event.target
    item = event.other
    if item.type == "mushroom":
        # "scale" changes the visual size of the unit.
        player.scale = 2
        game.powerEndTime = game.time + game.powerDuration
        player.say("ARRRGH!!!")

# The event handler for the "collide" event.
def onCollide(event):
    # The event owner. Who has collided.
    player = event.target
    # The colliding object.
    other = event.other
    # If it's a fence.
    if other.type == "fence":
        if player.scale == 2:
            # Destroy the fence.
            other.destroy()
            pass

# Use "collide" event to track collisions for the hero.
hero.on("collide", onCollide)
# Assign the event handler for hero on the "collect" event.
hero.on("collect", onCollect)

def checkTimers():
    # If game time is greater than game's powerEndTime
    # and the hero's scale is 2: 
    if hero.scale==2 and game.time>game.powerEndTime:
        # Set the hero's scale to 1.
        hero.scale = 1
    pass

while True:
    checkTimers()

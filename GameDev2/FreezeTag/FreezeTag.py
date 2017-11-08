# https://codecombat.com/play/level/freeze-tag
# Let's make the Tag game.

# We should count tagged archers.
game.tagged = 0
ui.track(game, "tagged")
goal = game.addManualGoal("Tag all archers.")

# Our players.
game.spawnXY("archer", 12, 52)
game.spawnXY("archer", 12, 34)
game.spawnXY("archer", 12, 16)
game.spawnXY("archer", 24, 52)
game.spawnXY("archer", 24, 34)
game.spawnXY("archer", 24, 16)
game.spawnXY("archer", 36, 52)
game.spawnXY("archer", 36, 34)
game.spawnXY("archer", 36, 16)

hero = game.spawnHeroXY('captain', 68, 24)
hero.maxSpeed = 20
# To increase the colliding size.
hero.scale = 2

# It sets the speed and behavior for archers.
def onSpawn(event):
    unit = event.target
    unit.behavior = "Scampers"
    unit.maxSpeed = 10

game.setActionFor("archer", "spawn", onSpawn)

# The event handler for "collide" events.
def onCollide(event):
    # The event owner who has collided with something.
    unit = event.target
    # The object the unit collided with.
    other = event.other
    # The behavior is a marker for the current state.
    # If the unit isn't tagged.
    if unit.behavior == "Scampers":
        # If "other" is the player.
        if other == hero:
            other.say("Freeze!")
            # Set unit.behavior to "Defends":
            unit.behavior = "Defends"
            # Increase game.tagged by 1:
            game.tagged +=1
            pass
    if unit.behavior == "Defends":
        # If other's type is "archer":
        if other.type == 'archer':
            # Set unit.behavior to "Scampers":
            unit.behavior = "Scampers"
            # Reduce game.tagged by 1.
            game.tagged -= 1
        pass

# Assign onCollide to the "collide" event for "archer"s.
game.setActionFor("archer", "collide", onCollide)

while True:
    if game.tagged >= 9:
        goal.success = True

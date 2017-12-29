# Use a wraparound mechanic to ensure no one leaves the map.

# Cowardly enemies.
generator = game.spawnXY("generator", 36, 34)
generator.spawnType = "munchkin"
generator.spawnAI = "Scampers"

# The hero, goals and UI.
hero = game.spawnHeroXY("captain", 12, 12)
hero.maxSpeed = 30
game.addDefeatGoal(6)
game.defeated = 0
ui.track(game, "defeated")

# This tracks positions of units and teleports them.
def onUpdate(event):
    unit = event.target
    # If the unit passed too far to the left.
    if unit.pos.x < 10:
        # Then we teleport it to the right.
        unit.pos.x = 68
    # If unit.pos.x greater than 70:
    if unit.pos.x > 70:
        # Set unit.pos.x to 12:
        unit.pos.x = 12
    # If the unit's Y coordinate less than 10:
    if unit.pos.y < 10:
        # Set unit.pos.y to 56:
        unit.pos.y = 56
    # If the unit's Y coordinate greater than 58:
    if unit.pos.y > 58:
        # Set the unit's Y coordiante to 12:
        unit.pos.y = 12

# This counts defeated enemies for UI.
def onDefeat(event):
    game.defeated += 1

# The hero and ogres can use the same event handlers.
hero.on("update", onUpdate)
game.setActionFor("munchkin", "defeat", onDefeat)
game.setActionFor("munchkin", "update", onUpdate)

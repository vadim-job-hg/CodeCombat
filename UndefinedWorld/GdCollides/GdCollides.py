# https://codecombat.com/play/level/gd-collides
# Spawn chest and keys
goldChest = game.spawnXY("gold-chest", 36, 14)
game.spawnXY("bronze-key", 12, 14)
# Create two more chest: "silver-chest" and "bronze-chest"
# Save results as variables silverChest and bronzeChest:
silverChest = game.spawnXY("silver-chest", 12, 52)
bronzeChest = game.spawnXY("bronze-chest", 68, 52)
# Create two more keys: "gold-key" and "silver-key"
game.spawnXY("gold-key", 32, 52)
game.spawnXY("silver-key", 52, 52)

hero = game.spawnHeroXY('captain', 60, 26)
hero.maxSpeed = 30
# chestGoal = game.addManualGoal("Collect 3 gems.")
chestCounter = 0

def openChest(actor, chest):
    # Chests have "open" method.
    chest.open()
    # TODO: I don't like it.
    item = actor.peekItem()
    item.destroy()
    actor.dropItem(chest)
    actor.say(chest + " is open!")
    # Increase chestCounter by 1:
    chestCounter += 1

def onCollide(event):
    # The owner of the event handler.
    player = event.target
    # The collider has collided with event.other .
    other = event.other
    # Use "peekItem" method to check carried items.
    item = player.peekItem()
    # Open chests has boolean property "isOpen".
    if not other.isOpen and item:
        # If its type is "gold-chest" and collider "hasGoldKey".
        if other.type == "gold-chest" and item.type == "gold-key":
            # Open the gold chest.
            openChest(player, other)
        # If its type is "silver-chest" and collider "hasSilverKey".
        elif other.type == "silver-chest" and item.type == "silver-key":
            # Open the silver chest.
            openChest(player, other)
        # Repeat for "bronze-chest" and "hasBronzeKey":
        elif other.type == "bronze-chest" and item.type == "bronze-key":
            openChest(player, other)

# Assing "collide" event for the hero:
hero.on("collide", onCollide)

def checkGoal():
    if chestCounter == 3:
        # chestGoal.complete = True
        hero.say("I've opened them all!")

while True:
    checkGoal()

# https://codecombat.com/play/level/alchemic-stack
# Use mushrooms to defeat the Yeti.
# Use potions to heal the hero.
yeti = hero.findNearestEnemy()
peasant = hero.findFriends()[0]
# Use "pickUpItem" command to take items.
items = peasant.findItems()
for item in items:
    if item.type!="gold-key":
        hero.command(peasant, "pickUpItem", item)
# Use "dropItem" command to put the top item.
# Drop the key near the door to open it.
key = peasant.findNearestByType("gold-key")
hero.command(peasant, "pickUpItem", key)
hero.command(peasant, "dropItem", Vector(40, 36))
# Use peasant.peekItem() to get know the item on the top.
# Mushrooms to the yeti, potions to the hero.
while True:
    item = peasant.peekItem()
    if not(item):
        break
    if item.type == "potion":
        hero.command(peasant, "dropItem", hero.pos)
    elif item.type == "mushroom":
        hero.command(peasant, "dropItem", yeti.pos)
# Aaaand one (or two) final hit to the yeti.
while True:
    hero.attack(yeti)

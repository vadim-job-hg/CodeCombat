# https://codecombat.com/play/level/stack-triage
# Sort out and deliver items:
# Yak - potion, Yeti - mushroom, Skeleton - lightstone.
yetiPos = {"x": 60, "y": 36}
yakPos = {"x": 40, "y": 52}
skeletonPos = {"x": 58, "y": 56}

peasant = hero.findFriends()[0]
items = peasant.findItems()
for item in items:
    # Command the peasant "pickUpItem" an item:
    hero.command(peasant, "pickUpItem", item)
    pass

while True:
    # Check an item on the top of the stack.
    topItem = peasant.peekItem()
    if not topItem:
        break
    # If topItem type is "potion":
    if topItem.type is "potion":
        # Command to "dropItem" it to yaks:
        hero.command(peasant, "dropItem", yakPos)
    # If topItem type is "mushroom":
    if topItem.type is "mushroom":
        # Command to "dropItem" to yetis:
        hero.command(peasant, "dropItem", yetiPos)
    # If topItem type is "lightstone":
    if topItem.type is "lightstone":
        # Command to "dropItem" to skeletons:
        hero.command(peasant, "dropItem", skeletonPos)


# https://codecombat.com/play/level/bait-and-switch

# Lure ogres in traps.

# The function makes the hero collect enough gold.
def collectUntil(enoughGold):
    # While the hero's gold less than enoughGold:
    while enoughGold>hero.gold:
        # Find a coin and take it:
        item = hero.findNearestItem()
        hero.move(item.pos)
    pass

# Collect gold for one decoy and build it on the red mark.
collectUntil(25)
hero.buildXY("decoy", 40, 52)
# It's better to hide.
hero.moveXY(20, 52)
# Use collectEnough function to collect 50 gold:
collectUntil(50)
# Build a decoy on the bone mark:
hero.buildXY("decoy", 68, 22)
# Build a decoy on the wooden mark:
hero.buildXY("decoy", 30, 20)

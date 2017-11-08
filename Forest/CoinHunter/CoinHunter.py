# https://codecombat.com/play/level/coin-hunter
# If you want to be a good hunter you need be patient.
# To make the training more interesting Senick poisoned you.
# While you aren't moving the poison is harmless.


# This function checks if a coin is closer than 20 meters.
def isCoinClose(coin):
    # Find the distance to the coin.
    distance = hero.distanceTo(coin)
    # If the distance less than 20:
    if distance<20:
        # Return True
        return True
    # Else:
    else:
        # Return False
        return False
    pass

while True:
    #item = hero.findNearestItem()
    item = hero.findNearestItem()
    if item:
        # If the item is close enough, then move and take it.
        if isCoinClose(item):
            # Pick up the item.
            hero.moveXY(item.pos.x, item.pos.y)
            pass

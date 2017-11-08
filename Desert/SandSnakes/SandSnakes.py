# This field is covered in firetraps.  Thankfully we've sent a scout ahead to find a path.  He left coins along the path so that if we always stick to the nearest coin, we'll avoid the traps.

# This canyon seems to interfere with your findNearest glasses!
# You'll need to find the nearest coins on your own.

while True:
    coins = hero.findItems()
    coinIndex = 0
    nearest = None
    nearestDistance = 9999

    # Loop through all the coins to find the nearest one.
    while coinIndex < len(coins):
        coin = coins[coinIndex]
        coinIndex += 1
        distance = hero.distanceTo(coin)
        if (distance < nearestDistance):
            nearest = coin
            nearestDistance = distance
            # If this coin's distance is less than the nearestDistance
            # Set nearest to coin
            # Set nearestDistance to distance
    hero.moveXY(nearest.pos.x, nearest.pos.y)
    # If there's a nearest coin, move to its position. You'll need moveXY so you don't cut corners and hit a trap.

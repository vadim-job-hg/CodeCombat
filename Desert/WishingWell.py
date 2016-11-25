# http://codecombat.com/play/level/wishing-well
# You need exactly 104 gold.
# Calculate how much gold is on the field, and say the phrases to increase or decrease the amount.

less = "Nimis"
more = "Non satis"
requiredGold = 104


# This function calculates the sum of coin values.
def sumCoinValues(coins):
    i = 0
    total = 0
    while i < len(coins):
        total += coins[i].value
        i += 1
    return total


while True:
    items = hero.findItems()
    goldAmount = sumCoinValues(items)
    if len(items) != 0:
        # If there is not enough gold, then say "Non satis".
        if goldAmount > 104:
            # If there is too much gold, then say "Nimis".
            hero.say(less)
        # If there is exactly 104 gold, then collect all coins.
        if goldAmount < 104:
            hero.say(more)
        pass
        if goldAmount == 104:
            break
while True:
    items = hero.findItems()
    item = hero.findNearest(items)
    if item:
        hero.move(item.pos)

# https://codecombat.com/play/level/golden-mirage
# Collect 7 real coins.
# Real coins have a unique value in the each group of coins.
# If a coin has the same value as another coin in the group, then it's a fake.
# Fake coins will transform into venomous creatures to hurt the player!
def Coin(coins):
    for coin1 in coins:
        count = 0
        for coin2 in coins:
            if coin1.value == coin2.value:
                count = count + 1
        if count == 1:
            return coin1


while True:
    coins = hero.findItems()
    if coins and len(coins):
        # The following code will help you debug:
        coin = Coin(coins)
        hero.say(coin.value);
        hero.moveXY(coin.pos.x, coin.pos.y);
        # When ready, delete the previous code and solve.

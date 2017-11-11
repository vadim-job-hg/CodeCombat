# https://codecombat.com/play/level/mad-maxer-gets-greedy
# Монеты исчезаю через несколько секунд!
# Собери все золотые монеты до того, как они исчезнут.

while True:
    closestGold = None
    minGoldDist = 9001
    coinIndex = 0
    coins = hero.findItems()
    # Найди ближайшую золотую монетку.
    # Запомни: золотая монета имеет значение - 3.
    for coin in coins:
        dist = hero.distanceTo(coin)/coin.value
        if minGoldDist > dist:
            closestGold = coin
            minGoldDist = dist
    if closestGold:
        # А теперь доберись до ближайшей золотой монетки и возьми её!
        hero.move(closestGold.pos)
        pass


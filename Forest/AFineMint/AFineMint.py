def pickUpCoin():
    coin = hero.findNearestItem()
    if coin:
        hero.moveXY(coin.pos.x, coin.pos.y)

def attackEnemy():
    enemy = hero.findNearestEnemy()
    if enemy:
        hero.attack(enemy)

while True:
    attackEnemy()
    pickUpCoin()

# http://codecombat.com/play/level/while-ogres-were-sleeping
# Enemies are sleeping. It's the perfect time for sabotage!
# Be careful and stay on the route.
# Kill the weak ogres with a deadly strike!
# Collect only the cheap coin. Don't be greedy!

step = 0


# This is how the hero moves around the level:
def moveHero(stage):
    if stage == 0:
        hero.moveXY(9 + step * 12, 8)
    elif stage == 1:
        hero.moveXY(68, 8 + (step - 5) * 10)
    elif stage == 2:
        hero.moveXY(68 - (step - 10) * 12, 58)
    return step + 1


while step < 5:
    step = moveHero(0)
    enemy = hero.findNearestEnemy()
    # If the enemy is an ogre and has less than 10 health, attack it!
    if enemy.team == "ogres" and enemy.health < 10:
        hero.attack(enemy)

while step < 5:
    step = moveHero(0)
    enemy = hero.findNearestEnemy()
    # If the enemy is an ogre and has less than 10 health:
    if enemy.team == "ogres" and enemy.health < 10:
        hero.attack(enemy)

while step < 10:
    step = moveHero(1)
    # coin = hero.findNearestItem()
    coin = hero.findNearestItem()
    # If the coin's value is less than 5 and is closer than 7 meters:
    if coin and hero.distanceTo(coin) < 7 and coin.value < 5:
        hero.moveXY(coin.pos.x, coin.pos.y)

while step < 15:
    step = moveHero(2)
    enemy = hero.findNearestEnemy()
    # If the enemy has less than 10 health and is closer than 7 meters:
    if enemy and enemy.health < 10 and hero.distanceTo(enemy) < 7:
        hero.attack(enemy)

hero.moveXY(10, 60)

# https://codecombat.com/play/ladder/wakka-maul
# Welcome to Wakka Maul! Prepare for combat!
# Venture through the maze and pick up gems to fund your warchest.
# Break down doors to unleash allies (or enemies).
# For example, to attack the door labeled "g" use:
# hero.attack("g")
# If you have enough gold, you can call out for help by saying the type of unit you would like to summon!
# hero.say("soldier") to summon a Soldier at the cost of 20 gold!
# hero.say("archer") to summon an Archer at the cost of 25 gold!
def attack():
    enemy = hero.findNearestEnemy()
    while enemy and enemy.health > 0:
        hero.attack(enemy)


hero.moveDown()
attack()
hero.moveRight()
attack()
hero.attack("g")
attack()
hero.say("soldier")
attack()
hero.moveRight(4)
attack()
hero.say("archer")
attack()
hero.moveUp()
attack()
hero.attack("h")
attack()
hero.attack("i")
attack()
hero.moveDown()
attack()
hero.moveRight(2)
attack()
hero.moveUp(5)
attack()
hero.say("soldier")
attack()
hero.say("soldier")
attack()

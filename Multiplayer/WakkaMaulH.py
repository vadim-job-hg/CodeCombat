#https://codecombat.com/play/ladder/wakka-maul
# Welcome to Wakka Maul! Prepare for combat!
# Venture through the maze and pick up gems to fund your warchest.
# Break down doors to unleash allies (or enemies).
# For example, to attack the door labeled "g" use:
#self.attack("g")
# If you have enough gold, you can call out for help by saying the type of unit you would like to summon!
#self.say("soldier") to summon a Soldier at the cost of 20 gold!
#self.say("archer") to summon an Archer at the cost of 25 gold!
def attack():
    enemy = self.findNearestEnemy()
    while enemy and enemy.health>0:
        self.attack(enemy)
self.moveDown()
attack()
self.moveRight()
attack()
self.attack("g")
attack()
self.say("soldier")
attack()
self.moveRight(4)
attack()
self.say("archer")
attack()
self.moveUp()
attack()
self.attack("h")
attack()
self.attack("i")
attack()
self.moveDown()
attack()
self.moveRight(2)
attack()
self.moveUp(5)
attack()
self.say("soldier")
attack()
self.say("soldier")
attack()


# https://codecombat.com/play/ladder/wakka-maul
# Welcome to Wakka Maul! Prepare for combat!
# Venture through the maze and pick up gems to fund your warchest.
# Break down doors to unleash allies (or enemies).
# For example, to attack the door labeled "g" use:
#hero.attack("g")
# If you have enough gold, you can call out for help by saying the type of unit you would like to summon!
#hero.say("soldier") to summon a Soldier at the cost of 20 gold!
#hero.say("archer") to summon an Archer at the cost of 25 gold!
def attack():
    enemy = hero.findNearestEnemy()
    while enemy and enemy.health>0:
        hero.attack(enemy)
move = [['down',1],['right',1], ['attack','g'],['right',1],['up',2], ['say', 'archer'], ['say', 'archer'], ['say', 'archer'], ['say', 'archer'], ['say', 'archer'],['right',3],['say', 'soldier'],['down',1], ['attack','h'], ['attack','i'],['up',3],['say', 'soldier'],['say', 'soldier'],['say', 'soldier'],['say', 'soldier'],['say', 'soldier'],['say', 'soldier'],['say', 'soldier'],['say', 'soldier'],['say', 'soldier'],['left',1], ['attack','e'],['down',1],['left',1], ['attack','f'],['down',3]]
index = 0
while index<len(move):
    if move[index][0]=='right':
        hero.moveRight(move[index][1])
    elif move[index][0]=='left':
        hero.moveLeft(move[index][1])
    elif move[index][0]=='up':
        hero.moveUp(move[index][1])
    elif move[index][0]=='down':
        hero.moveDown(move[index][1])
    elif move[index][0]=='say':
        hero.say(move[index][1])
    else:
        hero.attack(move[index][1])
    index = index + 1
while True:
    attack()
    hero.say('soldier')

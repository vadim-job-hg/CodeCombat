# http://codecombat.com/play/level/friend-and-foe
# Peasants and peons are gathering in the forest.
# Command the peasants to battle and the peons to go away!

while True:
    friend = hero.findNearestFriend()
    if friend:
        hero.say("To battle, " + friend.id + "!")
    # Now find the nearest enemy and tell them to go away.
    enemy = hero.findNearestEnemy()
    if enemy:
        hero.say("To go away, " + enemy.id + "!")

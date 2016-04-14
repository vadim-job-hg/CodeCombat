#http://codecombat.com/play/level/friend-and-foe
# Peasants and peons are gathering in the forest.
# Command the peasants to battle and the peons to go away!

while True:
    friend = self.findNearestFriend()
    if friend:
        self.say("To battle, " + friend.id + "!")
    # Now find the nearest enemy and tell them to go away.
    enemy = self.findNearestEnemy()
    if enemy:
        self.say("To go away, " + enemy.id + "!")

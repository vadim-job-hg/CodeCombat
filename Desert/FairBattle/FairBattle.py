# http://codecombat.com/play/level/fair-battle
# Today is the day for a fair battle!
# Wait until the total health of your soldiers is greater than ogre's.
# Don't attack while your soldiers don't have the advantage.

# Write a function to return the sum of health of an array:
def Calc(friends, enemies):
    frh = 0
    enh = 0
    for friend in friends:
        frh = frh + friend.health
    for enemy in enemies:
        enh = enh + enemy.health
    return frh > enh


while True:
    friends = hero.findFriends()
    enemies = hero.findEnemies()
    # Calculate and compare the total health of your soldiers and the ogres.
    if Calc(friends, enemies):
        hero.say("Attack")
        # Say "Attack" when you are ready.

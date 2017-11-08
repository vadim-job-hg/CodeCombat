# http://codecombat.com/play/level/reindeer-wakeup
# This array contains the 'asleep' or 'awake' status for each reindeer.
deerStatus = ['asleep', 'asleep', 'asleep', 'asleep', 'asleep']

# And this array contains our reindeer.
friends = hero.findFriends()

# Loop through all the reindeer and see which ones are awake.
for deerIndex in range(len(friends)):
    reindeer = friends[deerIndex]

    # If the reindeer's Y position is greater than 30, it's out of its pen.
    # If this is the case, set the reindeer's entry in the deerStatus array to 'awake'.
    if reindeer.pos.y > 30:
        deerStatus[deerIndex] = 'awake'
    pass

# Loop through statuses and report to Merek.
for statusIndex in range(len(deerStatus)):
    reindeer = friends[deerIndex]
    # Tell Merek the reindeer index and whether it's asleep or awake.
    # Say something like "Reindeer 2 is asleep" or "Reindeer 4 is awake"
    hero.say('Reindeer ' + statusIndex + ' is ' + deerStatus[statusIndex])
    pass

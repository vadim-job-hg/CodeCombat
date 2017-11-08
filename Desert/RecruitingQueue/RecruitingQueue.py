# https://codecombat.com/play/level/recruiting-queue
# Call peasants one after another.

# Neutral units are detected as enemies.
neutrals = hero.findEnemies()
while True:
    if len(neutrals):
        # Say the first peasant in the array of neutral units.
        hero.say(neutrals[0].id)
        pass
    else:
        hero.say("Nobody here")
    # Reassign "neutrals" with "findEnemies" method again.
    neutrals = hero.findEnemies()

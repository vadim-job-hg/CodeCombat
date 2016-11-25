# http://codecombat.com/play/ladder/sky-span
# This is your commander's code. Decide which unit to build each frame.
# Destroy the enemy base within 90 seconds!
# Check out the Guide at the top for more info.

#### 1. Choose your hero. ###########################################
# Heroes cost 100 gold. You start with 100 and earn 10 per second.

hero = 'tharin'
# hero = 'tharin'  # A fierce knight with battlecry abilities, type 'knight'.
# hero = 'hushbaum'  # A fiery spellcaster hero, type 'librarian'.
# hero = 'anya';  # A stealthy ranged attacker, type 'captain'.
if (hero and not hero.builtHero):
    hero.builtHero = hero.build(hero)
    return

#### 2. Choose which unit to build each turn. #######################
# Soldiers are hard-to-kill, low damage melee units who cost 20 gold.
# Archers are fragile but deadly ranged units who cost 25 gold.
# Units you build will go into the hero.built list.

buildOrder = ['archer', 'soldier']
buildType = buildOrder[len(hero.built) % len(buildOrder)]
if hero.buildables[buildType].goldCost <= hero.gold:
    hero.build(buildType)

####### 3. Command minions to implement your tactics. ################
# Minions obey 'move' and 'attack' commands.
# Click on a minion to see its API.

minions = hero.getFriends()
for minion in minions:
    if hero.commandableTypes.indexOf(minion.type) == -1:  # TODO: fix Python in
        # if not (minion.type in hero.commandableTypes):
        continue  # You can't command heroes.
    # hero.command(minion, 'move', {"x": 70, "y": 30})
    hero.command(minion, 'attack', minion.getNearestEnemy())

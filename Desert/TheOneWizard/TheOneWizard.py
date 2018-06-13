# Defeat as many ogres as you can.
# Use 'cast' and 'canCast' for spells.
index = 0
plan = ["lightning-bolt", 'attack', 'attack', 'attack', 'attack', 'attack', "lightning-bolt", "chain-lightning",
        "regen", 'attack', "regen", "lightning-bolt", "chain-lightning", 'attack', 'attack', "lightning-bolt", 'attack',
        "regen", "lightning-bolt", 'say', "away", 'armagedon']
while True:
    current_plan = plan[index % len(plan)]
    if (current_plan == 'regen'):
        if hero.isReady("regen"):
            hero.cast("regen", hero)
            index += 1
        else:
            hero.moveXY(8, 30)
    elif (current_plan == 'away'):
        hero.moveXY(18, 41)
        index += 1
    elif (current_plan == 'say'):
        hero.say("booring")
        index += 1
    elif (current_plan == 'armagedon'):
        hero.moveXY(7, 41)
        index += 1
    else:
        enemy = hero.findNearestEnemy()
        if (enemy):
            if (enemy and enemy.health > 0):
                dist = hero.distanceTo(enemy)
                if (current_plan == 'attack'):
                    hero.attack(enemy)
                elif (current_plan == "chain-lightning" and hero.isReady("chain-lightning")):
                    hero.cast("chain-lightning", enemy)
                elif current_plan == "lightning-bolt" and hero.isReady("lightning-bolt"):
                    hero.cast("lightning-bolt", enemy)
            if (enemy.health <= 0):
                index += 1
        else:
            hero.moveXY(8, 30)





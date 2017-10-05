#https://codecombat.com/play/level/difficulty-coin?
# Create a hero
hero = game.spawnHeroXY('knight', 40, 47)
hero.maxHealth = 1500
hero.maxSpeed = 10

# Create three coins to collect.
copperCoin = game.spawnXY('bronze-coin', 26, 33)
silverCoin = game.spawnXY('silver-coin', 44, 28)
goldCoin = game.spawnXY('gold-coin', 60, 44)

# Create a manual goal to collect one coin.
chooseGoal = game.addManualGoal('Choose wisely')
game.addDefeatGoal()
game.addSurviveGoal()
game.difficulty = '...'

# Add visuals
ui.track(game, 'difficulty')
ui.track(game, 'score')
hero.say('Which should I choose...')


def onCollect(event):
    # When the hero collects a coin, destroy the other
    # two and build the level based on difficulty choice.
    item = event.other
    if item.type == 'coin':
        if item.value == 1:
            game.difficulty = 'Easy'
            silverCoin.destroy()
            goldCoin.destroy()
        if item.value == 2:
            game.difficulty = 'Medium'
            # Destroy the copper and gold coins
            goldCoin.destroy()
            copperCoin.destroy()
        if item.value == 3:
            pass
            # Set game difficulty to "Impossible"
            game.difficulty = 'Impossible'
            # Destroy the silver and gold coins
            goldCoin.destroy()
            silverCoin.destroy()
        beginFight()
        # Set chooseGoal.success to True
        chooseGoal.success = True


hero.on('collect', onCollect)


def beginFight():
    if game.difficulty == 'Easy':
        # Create a few barriers and weak enemies
        game.spawnXY('forest', 56, 54)
        game.spawnXY('forest', 56, 46)
        game.spawnXY('forest', 56, 38)
        game.spawnXY('forest', 9, 23)
        game.spawnXY('forest', 17, 23)
        game.spawnXY('forest', 25, 23)

        ogre1 = game.spawnXY('munchkin-m', 11, 14)
        ogre1.behavior = "AttacksNearest"
        ogre2 = game.spawnXY('munchkin-m', 67, 51)
        ogre2.behavior = "AttacksNearest"
        ogre3 = game.spawnXY('munchkin-m', 66, 13)
        ogre3.behavior = "AttacksNearest"

        hero.say('This battle is laughably easy!')

    if game.difficulty == 'Medium':
        # Create medium-difficulty enemies in a maze
        game.spawnMaze(21)
        ogre = game.spawnXY('ogre-f', 45, 43)
        ogre.behavior = "AttacksNearest"
        ogre = game.spawnXY('ogre', 42, 40)
        ogre.behavior = "AttacksNearest"

        ogre = game.spawnXY('munchkin', 60, 13)
        ogre.behavior = "AttacksNearest"
        ogre = game.spawnXY('munchkin', 60, 19)
        ogre.behavior = "AttacksNearest"
        ogre = game.spawnXY('archer-f', 13, 28)
        ogre.behavior = "AttacksNearest"
        ogre = game.spawnXY('archer-f', 13, 44)
        ogre.behavior = "AttacksNearest"

        hero.say('This is non-trivial...')

    if game.difficulty == 'Impossible':
        # Create a cluster of various enemies,
        # with nowhere to hide!
        i = 0
        while i < 20:
            randomUnit = game.randomInteger(0, 9)
            randomX = game.randomInteger(13, 60)
            randomY = game.randomInteger(13, 60)
            if randomUnit >= 8:
                unitType = 'ogre'
            elif randomUnit >= 6:
                unitType = 'thrower'
            else:
                unitType = 'munchkin'
            unit = game.spawnXY(unitType, randomX, randomY)
            unit.behavior = 'AttacksNearest'
            i += 1

        hero.say("Oh I'm in trouble...")


def onDefeat(event):
    # Keep score. The harder the difficulty, the
    # higher the score can be!
    if event.target.type == 'munchkin':
        game.score += 1
    if event.target.type == 'thrower':
        pass
        # Add 3 to the game score.
        game.score += 3
    # if the target is an 'ogre'
    if event.target.type == 'ogre':
        # add 10 to the game score
        game.score += 10
    hero.say('defeated ' + event.target.type)


# Add the event handlers
game.setActionFor("munchkin", "defeat", onDefeat)
game.setActionFor("ogre", "defeat", onDefeat)
game.setActionFor("headhunter", "defeat", onDefeat)

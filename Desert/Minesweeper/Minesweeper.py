# http://codecombat.com/play/level/minesweeper?course=56462f935afde0c6fd30fc8c&course-instance=56fc25d7263b0220002aff0e
# Проведи крестьян и лекаря через минное поле.

while True:
    coin = hero.findNearestItem()
    healingThreshold = hero.maxHealth / 2
    # Check to see if you are critically injured.
    if hero.health < healingThreshold:
        # Move left 10m.
        hero.moveXY(hero.pos.x - 10, hero.pos.y)
        # Ask for a heal.
        hero.say("Can I get a heal?")
        pass
    # Else, move to the next coin.
    elif coin:
        hero.moveXY(coin.pos.x, coin.pos.y)

#http://codecombat.com/play/level/minesweeper?course=56462f935afde0c6fd30fc8c&course-instance=56fc25d7263b0220002aff0e
# Проведи крестьян и лекаря через минное поле.

while True:
    coin = self.findNearestItem()
    healingThreshold = self.maxHealth / 2
    # Check to see if you are critically injured.
    if self.health < healingThreshold:
        # Move left 10m.
        self.moveXY(self.pos.x - 10, self.pos.y)
        # Ask for a heal.
        self.say("Can I get a heal?")
        pass
    # Else, move to the next coin.
    elif coin:
        self.moveXY(coin.pos.x, coin.pos.y)

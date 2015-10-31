# Призови несколько солдат и отправь их на базу.

# Каждый солдат стоит 20 золотых.
while self.gold > self.costOf("soldier"):
    self.summon("soldier")
    
# Добавь цикл while для командования всеми солдатами.
soldiers = self.findFriends()
soldierIndex = 0
while soldierIndex<len(soldiers):
    soldier = soldiers[soldierIndex]
    self.command(soldier, "move", {"x": 50, "y": 40})
    soldierIndex +=1

# Присоединись к боевым товарищам!
self.moveXY(50,43)

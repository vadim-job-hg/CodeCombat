# Проводим полевые испытания нового возводимого объекта - приманки.
# Постройте 4 приманки и сообщите их количество Нарье.
decoysBuilt = 0
goldAmount = 0
while True:
    item = self.findNearestItem()
    self.moveXY(item.pos.x, item.pos.y)
    # Loot the coin!
    goldAmount = self.gold
    # Каждая приманка стоит 25 золотых. Используйте Quartz Sense Stone
    # чтобы узнать когда наберёте больше 25 золотых self.gold.
    if (goldAmount >= 25):
        self.buildXY('decoy', item.pos.x, item.pos.y)
        # Считайте количество уже построенных приманок.
        decoysBuilt += 1
    # Прерывайте цикл когда построите 4.
    if (decoysBuilt == 4):
        break
    self.say("Приманки построены!")
    # Идите к Нарье и сообщите сколько приманок построено.
    self.moveXY(14, 36)
    self.say(decoysBuilt)

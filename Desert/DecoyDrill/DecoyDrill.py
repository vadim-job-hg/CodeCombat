# Проводим полевые испытания нового возводимого объекта - приманки.
# Постройте 4 приманки и сообщите их количество Нарье.
decoysBuilt = 0
goldAmount = 0
while True:
    item = hero.findNearestItem()
    hero.moveXY(item.pos.x, item.pos.y)
    # Loot the coin!
    goldAmount = hero.gold
    # Каждая приманка стоит 25 золотых. Используйте Quartz Sense Stone
    # чтобы узнать когда наберёте больше 25 золотых hero.gold.
    if (goldAmount >= 25):
        hero.buildXY('decoy', item.pos.x, item.pos.y)
        # Считайте количество уже построенных приманок.
        decoysBuilt = decoysBuilt + 1
    # Прерывайте цикл когда построите 4.
    if (decoysBuilt == 4):
        break
hero.say("Приманки построены!")
# Идите к Нарье и сообщите сколько приманок построено.
hero.moveXY(14, 36)
hero.say(decoysBuilt)

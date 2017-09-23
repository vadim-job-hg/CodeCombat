# У тебя только 20 секунд до прихода толпы огров!
# Хватай столько монет, сколько сможешь и уноси ноги на базу, закрывая проход за собой!
while hero.now() < 30:
    item = hero.findNearestItem()
    if item:
        if (hero.isReady("jump") and hero.distanceTo > 15):
            hero.jumpTo(item.pos)
        else:
            hero.move(item.pos)
    if (hero.gold > 59):
        break

if (hero.isReady("jump")):
    hero.jumpTo({'x': 21, 'y': 38})
hero.moveXY(21, 38)
while hero.pos.x > 16:
    hero.move({'x': 15, 'y': 38})
hero.buildXY('fence', 20, 38)

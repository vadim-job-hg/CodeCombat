#  https://codecombat.com/play/level/timber-turncoat
while True:
    # Собирай золото.
    item = hero.findNearestItem()
    if item:
        hero.move(item.pos)
    # Если золота достаточно, призывай солдат.
    if hero.gold > hero.costOf("archer"):
        hero.summon("archer")
    # При помощи for-цикла отдавай приказы каждому солдату.
    for friend in hero.findFriends():
        if friend.type == "archer":
            enemy = friend.findNearestEnemy()
            # Если видишь врага прикажи атаковать.
            # Careful! If your soldiers are defeated, a warlock will appear!
            # Если нет, прикажи следовать в правую часть карты.
            if (enemy):
                hero.command(friend, "attack", enemy)
            else:
                hero.command(friend, "move", {'x': 69, 'y': 37})


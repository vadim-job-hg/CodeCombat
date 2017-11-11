# https://codecombat.com/play/level/yakstraction
# Защити Брэнди от нашествия жаждущих яков!
# Собирай золото, чтобы ставить приманки, отвлекающие яков.
# Используй флаги, чтобы решить, когда и где ставить приманки.

while True:
    flag = hero.findFlag()
    item = hero.findNearestItem()
    if flag:
        # Подберите флаг.
        hero.buildXY("decoy", flag.pos.x, flag.pos.y)
        hero.pickUpFlag(flag)
    elif item:
        hero.move(item.pos)


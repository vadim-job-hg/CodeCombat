# Try to get the best grade (gold) at the magic exam.
# Move to each X mark, then use a spell.
def action():
    friend = hero.findNearestFriend()
    if friend:
        if friend.type == 'soldier':
            hero.cast('heal', friend)
        elif friend.type == 'goliath':
            hero.cast('grow', friend)
        else:
            hero.cast('regen', friend)
    enemy = hero.findNearestEnemy()
    if enemy:
        if enemy.type == 'ogre':
            hero.cast('force-bolt', enemy)
        elif enemy.type == 'brawler':
            hero.cast('shrink', enemy)
        else:
            hero.cast('poison-cloud', enemy)


hero.moveXY(18, 24)
action()
hero.moveXY(18, 40)
action()
hero.moveXY(34, 24)
action()
hero.moveXY(34, 40)
action()
hero.moveXY(50, 40)
action()
hero.moveXY(50, 24)
action()
hero.moveXY(66, 40)
item = hero.findNearestItem()
hero.cast('grow', hero)
hero.moveXY(item.pos.x, item.pos.y)
hero.moveXY(66, 24)
item = hero.findNearestItem()
hero.moveXY(item.pos.x, item.pos.y)

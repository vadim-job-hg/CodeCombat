# Try to get the best grade (gold) at the magic exam.
# Move to each X mark, then use a spell.
hero.moveXY(18, 40)
friend = hero.findNearestFriend()
hero.cast('heal', friend)
hero.moveXY(18, 24)
enemy = hero.findNearestEnemy()
hero.cast('force-bolt', enemy)
hero.moveXY(34, 24)
enemy = hero.findNearestEnemy()
hero.cast('shrink', enemy)
hero.moveXY(34, 40)
friend = hero.findNearestFriend()
hero.cast('grow', friend)

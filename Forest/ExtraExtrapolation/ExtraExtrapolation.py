# http://codecombat.com/play/level/extra-extrapolation
shellAirTime = 3.4

ogre = hero.getNearestEnemy()
if (ogre):
    hero.attackXY(ogre.pos.x, ogre.pos.y)

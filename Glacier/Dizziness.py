# https://codecombat.com/play/level/dizziness
#  A Shadow Vortex will help against the ogre throwers.
hero.shadowVortex(Vector(20, 32), Vector(20, 36))
while True:
    # Don't forget about flankers. Be sure to fight:
    enemy = hero.findNearestEnemy()
    if enemy:
        hero.attack(enemy)
    
    brawlers = hero.findByType("brawler")
    # If you see a brawler and "shadow-vortex" is ready:
    if brawlers and hero.isReady('shadow-vortex'):
        # Create a vortex from (1, 1) to (80, 68):
        hero.shadowVortex(Vector(1, 1), Vector(80, 68))

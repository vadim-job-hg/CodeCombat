# http://codecombat.com/play/level/brewball
def avoidNearest(target):
    nearest = hero.findNearest(firetraps)
    h2t = Vector.subtract(target, hero.pos)
    h2n = Vector.subtract(nearest.pos, hero.pos)
    if hero.distanceTo(nearest) > 4:
        step = Vector.normalize(h2t)
        nPos = Vector.add(hero.pos, step)
        hero.moveXY(nPos.x, nPos.y)
        return

    angle1 = Vector.heading(h2t)
    angle2 = Vector.heading(h2n)

    if target.x < nearest.pos.x:
        angle1 = - angle1
        angle2 = - angle2
        angle1 = Math.PI - angle1
        angle2 = Math.PI - angle2

    # if Vector.heading(h2t) > Vector.heading(h2n):
    if angle1 > angle2:
        adVec = Vector.rotate(h2n, Math.PI / 2)
    else:
        adVec = Vector.rotate(h2n, - Math.PI / 2)
        pass
    nPos = Vector.add(hero.pos, adVec)
    hero.moveXY(nPos.x, nPos.y)


while True:
    potion = hero.findFriendlyMissiles()[0]
    firetraps = hero.findHazards()
    # Remember that a Fire Trap will trigger if you move closer than 3 meters!
    omarn = hero.findByType("potion-master")[0]
    if potion:
        dest = potion.targetPos
        # Go get the potion.
        avoidNearest(dest)

        pass
    else:
        if omarn and hero.distanceTo(omarn) > 10:
            # Move back to Omarn.
            avoidNearest(omarn.pos)

            # Warning: isPathClear doesn't work with Hazards!
            pass
        else:
            hero.say("Hup, hup!")


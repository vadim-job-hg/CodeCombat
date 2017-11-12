r = 10
diff = 0.5
threshold = 5.7
S = 3
circle = 5
cx = 68
cy = 68

def prepareMap():
    map = []
    for y in range(0, 135):
        row = []
        for x in range(0, 160):
            row.push(0)
        map.push(row)
    hazards = hero.findHazards()
    for hazar in hazards:
        hx = Math.round(hazar.pos.x)
        hy = Math.round(hazar.pos.y)
        map[hx][hy] = 1
    return map

def buildRect(x1, y1, x2, y2):
    if (x1 == x2):
        return [[x1 - S, y1], [x1 + S, y1], [x2 - S, y2], [x2 + S, y2]]
    tang = (y1 - y2) / (x1 - x2)
    ang = Math.atan(tang)

rad = Math.PI * 2 / 360
hero.moveXY(128 - r / 2 - diff, 68)
angle = 0
while True:
    if (not(circle)):
        break
    R = r * circle + r / 2 - diff
    iR = R - r
    while True:
        angle = (angle + 2) % 360
        x = cx + Math.cos(angle * rad) * R
        y = cy + Math.sin(angle * rad) * R
        ix = cx + Math.cos(angle * rad) * iR
        iy = cy + Math.sin(angle * rad) * iR
        hero.moveXY(x, y)
        nearest = hero.findNearest(hero.findHazards())
        if (hero.distanceTo(nearest) >= threshold):
            hero.debug(angle, hero.distanceTo(nearest))
            hero.moveXY(ix, iy)
            circle -= 1
            break




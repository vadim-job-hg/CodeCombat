while True:
    item = hero.findNearestItem() 
    if item:
        x = item.pos.x
        y = item.pos.y
        hero.blink(Vector(x, y))
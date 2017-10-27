# https://codecombat.com/play/level/darkhopper
# Collect 10 gems.

# Use "blink" ability to teleport between gaps.
while True:
    item = hero.findNearestItem() 
    if item:
        x = item.pos.x
        y = item.pos.y
        hero.blink(Vector(x, y))
    # hero.blink(thing.pos)
    
    pass

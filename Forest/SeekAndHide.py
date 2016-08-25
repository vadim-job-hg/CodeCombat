# https://codecombat.com/play/level/seek-and-hide
# Gather 4 lightstones to defeat the Brawler.
# Move along the outside of the camp, gathering the lightstones.


# The function should check for the item and move to hide.
# Complete the function:
def checkTakeHide(item):
    if item:
        # The item is here, take it.
        hero.moveXY(item.pos.x, item.pos.y)
        # Then hide. Move to the center of the camp.
        hero.moveXY(40, 34)
    enemy = hero.findNearestEnemy()

# Move to the right mark, then to the left one.
while True:
    # Move to the top right mark.
    hero.moveXY(68, 56)
    # Search for a stone there.
    stone = hero.findNearestItem()
    # Call the function 'checkTakeHide' with the argument 'stone'.
    checkTakeHide(stone)
    # Move to the top left mark, search for a stone, and call the function.
    hero.moveXY(12, 56)
    stone = hero.findNearestItem()
    checkTakeHide(stone)

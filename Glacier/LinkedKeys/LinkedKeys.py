# https://codecombat.com/play/level/linked-keys
# Open doors and collect the chest of gems.

# The nearest peasant has the first key.
peasantLinkedList = hero.findNearest(hero.findFriends())
doorIndex = 0
doorDistance = 12

# The list reference is the reference to the first element.
currentPeasant = peasantLinkedList
while True:
    pos = {"x": 20 + doorIndex * doorDistance, "y": 34}
    hero.command(currentPeasant, "dropItem", pos)
    hero.command(currentPeasant, "move", Vector(hero.pos.x+10+doorIndex, hero.pos.y))
    # Each element of the linked list "knows"
    # about the next element and store the link.
    currentPeasant = currentPeasant.next
    # If there is no next element then the list ends.
    if not currentPeasant:
        break
    # Increase "doorIndex" by 1.
    doorIndex +=1
hero.say('all')
# Doors are open. Action!
hero.moveXY(16, 34)
while True:
    enemy = hero.findNearestEnemy()
    item = hero.findNearestItem()
    if enemy:
        hero.attack(enemy)
    elif item:
        hero.move(item.pos)
    else:
        hero.moveXY(64, 34)

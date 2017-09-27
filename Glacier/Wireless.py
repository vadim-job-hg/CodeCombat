# https://codecombat.com/play/level/wireless
# Destroy the door and ogres.

# Backup robots are stronger.
def findBackupRobots():
    robots = hero.findByType("robot-walker")
    reserveRobots = []
    for robot in robots:
        if robot.health > 5000:
            reserveRobots.push(robot)
    return reserveRobots

# The function replaces a node in the list.
def replaceMissingLink(linkedList, broken, replacement):
    current = linkedList
    prev = None
    while current:
        if current == broken:
            if prev:
                # Use "setNext" to assign the next node.
                prev.setNext(replacement)
            # Set the next node for the replacement robot:
            replacement.setNext(current.next)
            break
        prev = current
        current = current.next

# This function finds a broken list elements.
def diagnoseList(linkedList):
    current = linkedList
    # Use "next" property to iterate the list.
    # If some robot ass dead, return that robot:
    while current:
        if current.health <= 0:
            #hero.say(current.health)
            return current
        current = current.next
    # If all are "healthy".
    return None

# The head of the linked list of robots.
robotList = hero.findNearest(hero.findFriends())
while True:
    backUpRobots = findBackupRobots()
    brokenRobot = diagnoseList(robotList)
    if brokenRobot and len(backUpRobots):
        replaceMissingLink(robotList, brokenRobot, backUpRobots[0])

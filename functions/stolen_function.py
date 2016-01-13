#https://github.com/cristoslc/CodeCombatSnippets/blob/master/python/findWorstEnemy.py
def findWorstEnemy():
    worstEnemyLists = {}
    worstEnemies = []

    enemies = self.findEnemies()
    attackOrder = ['thrower', 'shaman', 'ogre']

    worstEnemyLists['nobody'].append(None)

    for enemy in enemies:
        worstEnemyLists[enemy.type] = []
        worstEnemyLists[enemy.type].append(enemy)

    for eType in attackOrder:
        if len(worstEnemyLists[eType]) > 0:
            worstEnemy = self.findNearest(worstEnemyLists[eType])
            return worstEnemy

    return None
#https://github.com/sbandur84/CodeCombat-Levels-Code/blob/master/Dungeon_Cavern%20Survival.py
def runFrom(enemy):
    distance = 20
    x = enemy.pos.x
    y = enemy.pos.y
    myX = self.pos.x
    myY = self.pos.y
    # premikamo se po polju
    #smo na levem robu
    if myX - distance < minX:
        # če smo gori gre desno
        if myY + distance > maxY:
            self.moveXY(myX + distance, myY)
        # ali gor
        else:
            self.moveXY(myX, myY + distance)
    # pri zgornji
    elif myY + distance > maxY:
        # če smo že desno pojdi dol
        if myX + distance > maxX:
            self.moveXY(myX, myY - distance)
        # ali desno
        else:
            self.moveXY(myX + distance, myY)
    # pri desni
    elif myX + distance > maxX:
        # če smo spodaj idi levo
        if myY - distance < minY:
            self.moveXY(myX - distance, myY)
        # ali dol
        else:
            self.moveXY(myX, myY - distance)
    # pri spodnji
    elif myY - distance < minY:
        # če smo levo idi gor
        if myX - distance < minX:
            self.moveXY(myX, myY + distance)
        # ali levo
        else:
            self.moveXY(myX - distance, myY)
    else:
        #beži od sovražnika
        if x < maxX/2 and y < maxY/2:
            self.moveXY(myX + distance, myY + distance)
        if x > maxX/2 and enemy.pos.y < maxY/2:
            self.moveXY(myX - distance, myY + distance)
        if enemy.pos.x < maxX/2 and y > maxY/2:
            self.moveXY(myX + distance, myY - distance)
        if enemy.pos.x > maxX/2 and y > maxY/2:
            self.moveXY(myX - distance, myY - distance)
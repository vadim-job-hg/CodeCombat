def commandFriends():
#--------------------
    distance = 5
    friends = self.findFriends()
    
    for friend in friends:
        goalf = friendsPoint1
        action = 'move'
		
        goalf = Vector.subtract(goalf, friend.pos)
        goalf = Vector.normalize(goalf)
        goalf = Vector.multiply(goalf, distance)
        
        hazard = friend.findNearest(self.findHazards())
        if hazard and friend.distanceTo(hazard) < distance:
            vectorToH = Vector.subtract(friend.pos, hazard.pos)
            vectorToH = Vector.normalize(vectorToH)
            vectorToH = Vector.multiply(vectorToH, distance)
            goalf =  Vector.add(vectorToH, goalf)
        
        missile = friend.findNearest(self.findEnemyMissiles())
        if missile and friend.distanceTo(missile) < distance:
            vectorToH = Vector.subtract(friend.pos, missile.pos)
            vectorToH = Vector.normalize(vectorToH)
            vectorToH = Vector.multiply(vectorToH, distance)
            goalf =  Vector.add(vectorToH, goalf)
        
        if friend.type == 'paladin':
            self.command(friend, "shield")
        else:
            moveToPos = Vector.add(friend.pos, goalf)
            self.command(friend, action, moveToPos)
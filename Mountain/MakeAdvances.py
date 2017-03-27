# https://codecombat.com/play/level/make-advances
# Advance through the forgotten tomb.
# Be wary, traps lay in wait to ruin your day!

# The Paladins volunteer to lead the way.
# Command them to shield against incoming projectiles.
while True:
    friends = hero.findFriends()
    # findEnemyMissiles finds all dangerous projectiles.
    projectiles = hero.findEnemyMissiles()
    for friend in friends:
        if friend.type is "paladin":
            # Find the projectile nearest to the friend:
            projectile = friend.findNearest(projectiles)
            # If the projectile exists
            # AND is closer than 10 meters to the paladin:
            if projectile and friend.distanceTo(projectile) < 10:
                # Command the friend to "shield":
                hero.command(friend, 'shield')
            # ELSE, when there is no potential danger:
            else:
                # Advance the paladin:
                x = friend.pos.x + 10
                y = friend.pos.y
                hero.command(friend, 'move', {'x': x, 'y': y})
            pass
        else:
            # If not a paladin, just advance:
            pass
        pass
        # Advance the hero in the x direction:


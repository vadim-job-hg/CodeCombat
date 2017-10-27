# You cannot collect coins.
# Summon peasants to collect coins for you.
# Collecting coins spawns a growing 'tail' behind the peasants.
# When a peasant touches a tail, they die.
# Collect 200 gold to pass the level.
# The following APIs are available on your team's peasants: "snakeBackward"
# The following APIs are available on neutral peasants: "snakeBackward", "snakeHead", "snakeForward"
x = 10
direct = []
direct[0] = Vector(10, 0)
while True:
    friends = hero.findFriends()
    tails = hero.findEnemies()
    coins = hero.findItems()
    for friend in friends:
        if Math.floor(friend.pos.x > 10) and Math.floor(friend.pos.x) < 70:
            if Math.floor(friend.pos.y > 10) and Math.floor(friend.pos.y) < 55:
                if Math.floor(friend.pos.x) % 7 == 0:
                    if Math.floor(friend.pos.x) % 2 == 0:
                        direct[0] = Vector(0, 10)
                    else:
                        direct[0] = Vector(0, -10)
                else:
                    direct[0] = Vector(10, 0)
            else:
                if (friend.pos.y <= 10):
                    direct[0] = Vector(10, 2)
                else:
                    direct[0] = Vector(10, -2)
            direct[0] = Vector(0, 0)
            move = Vector.add(friend.pos, direct[0])
        else:
            if Math.floor(friend.pos.x < 60):
                move = {'x': 75, 'y': 60}
            elif(Math.floor(friend.pos.y > 10)):
                move = {'x': 75, 'y': 10}
            else:
                move = {'x': 10, 'y': 10}
        hero.command(friend, 'move', move)


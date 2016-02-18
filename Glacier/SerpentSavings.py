
# You cannot collect coins.
# Summon peasants to collect coins for you.
# Collecting coins spawns a growing 'tail' behind the peasants.
# When a peasant touches a tail, they die.
# Collect 500 coins to pass the level.
# The following APIs are available on your team's peasants: "snakeBackward"
# The following APIs are available on neutral peasants: "snakeBackward", "snakeHead", "snakeForward"


self.summon("peasant");
loop:
    friends = self.findFriends()
    tails = self.findEnemies()
    coins = self.findItems()
    for friend in friends:
        # Command the peasant to collect a coin, while avoiding the tails.
        
        pass

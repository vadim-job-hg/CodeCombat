# https://codecombat.com/play/level/mad-maxer-redemption
# Вы не можете защитить своих друзей!
# Прикажи им идти домой, где лучник сможет им помочь.

while True:
    weakestFriend = None
    leastHealth = 9999
    friendIndex = 0
    # Найди у кого из друзей самый низкий уровень здоровья.
    friends = hero.findFriends()
    for friend in friends:
        if leastHealth > friend.health and friend.type != 'archer':
            weakestFriend = friend
            leastHealth = friend.health
    # Скажи другу с самым низким уровнем здоровья, идти домой первым.
    if weakestFriend:
        hero.say('Hey ' + weakestFriend.id + ', go home!')

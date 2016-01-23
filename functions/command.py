def сommandTroops():    
    for index, friend in enumerate(self.findFriends()):
        if friend.type == 'archer':
            CommandArcher(friend)        
        elif friend.type == 'paladin':
            CommandPaladin(friend)   
        elif friend.type == 'soldier':
            CommandSoldier(friend)

def CommandPaladin(soldier):
    pass

def CommandSoldier(soldier):
    pass

def CommandArcher(soldier):
    pass
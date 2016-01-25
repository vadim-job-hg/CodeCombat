enemy_types = {}
enemy_types['shaman'] = {'danger':10, 'focus':100}
enemy_types['warlock'] = {'danger':10, 'focus':30}
enemy_types['arrow-tower'] = {'danger':10, 'focus':20}
enemy_types['catapult'] = {'danger':10, 'focus':100}
enemy_types['burl'] = {'danger':10, 'focus':20}
enemy_types['artillery'] = {'danger':10, 'focus':100}
enemy_types['witch'] = {'danger':8, 'focus':100}
enemy_types['brawler'] = {'danger':7, 'focus':55}
enemy_types['ogre'] = {'danger':5, 'focus':40}
enemy_types['chieftain'] = {'danger':6, 'focus':35}
enemy_types['fangrider'] = {'danger':4, 'focus':22}
enemy_types['skeleton'] = {'danger':5, 'focus':22}
enemy_types['thrower'] = {'danger':3, 'focus':22}
enemy_types['munchkin'] = {'danger':2, 'focus':15}
enemy_types['yak'] = {'danger':-1, 'focus':0}
enemy_types['ice-yak'] = {'danger':-1, 'focus':0}

def findTarget():
    danger = 0
    enemy_return = None
    for type in enemy_types.keys():
        if enemy_types[type].danger>danger:
            enemy =  self.findNearest(self.findByType(type))
            if enemy and self.distanceTo(enemy)<enemy_types[type].focus:
                enemy_return = enemy
                danger = enemy_types[type].danger
    if type is not None:
        enemy =  self.findNearest(self.findEnemies())
    return enemy_return


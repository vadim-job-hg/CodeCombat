enemy_types = {}
# humans hero types
enemy_types['knight'] = {'danger': 100, 'focus': 100}
enemy_types['ranger'] = {'danger': 100, 'focus': 100}
enemy_types['librarian'] = {'danger': 100, 'focus': 100}
enemy_types['potion-master'] = {'danger': 100, 'focus': 50}
enemy_types['goliath'] = {'danger': 100, 'focus': 50}
enemy_types['captain'] = {'danger': 100, 'focus': 100}
enemy_types['trapper'] = {'danger': 100, 'focus': 100}
enemy_types['samurai'] = {'danger': 100, 'focus': 50}
enemy_types['forest-archer'] = {'danger': 100, 'focus': 50}
enemy_types['sorcerer'] = {'danger': 100, 'focus': 50}
enemy_types['ninja'] = {'danger': 100, 'focus': 50}

# ogres types
enemy_types['shaman'] = {'danger': 10, 'focus': 100}
enemy_types['warlock'] = {'danger': 10, 'focus': 30}
enemy_types['arrow-tower'] = {'danger': 10, 'focus': 20}
enemy_types['catapult'] = {'danger': 10, 'focus': 100}
enemy_types['burl'] = {'danger': 10, 'focus': 20}
enemy_types['artillery'] = {'danger': 10, 'focus': 100}
enemy_types['witch'] = {'danger': 8, 'focus': 100}
enemy_types['brawler'] = {'danger': 7, 'focus': 55}
enemy_types['ogre'] = {'danger': 5, 'focus': 40}
enemy_types['chieftain'] = {'danger': 6, 'focus': 35}
enemy_types['fangrider'] = {'danger': 4, 'focus': 22}
enemy_types['skeleton'] = {'danger': 5, 'focus': 22}
enemy_types['scout'] = {'danger': 4, 'focus': 22}
enemy_types['thrower'] = {'danger': 3, 'focus': 22}
enemy_types['munchkin'] = {'danger': 2, 'focus': 15}
enemy_types['yak'] = {'danger': -1, 'focus': 0}
enemy_types['ice-yak'] = {'danger': -1, 'focus': 0}
if hero.team == 'humans':
    team = 'humans'
else:
    team = 'ogres'


def findTarget():
    danger = 0
    enemy_return = None
    for type in enemy_types.keys():
        if enemy_types[type].danger > danger:
            enemy = hero.findNearest(hero.findByType(type))
            if enemy and enemy.team != team and hero.distanceTo(enemy) < enemy_types[type].focus:
                enemy_return = enemy
                danger = enemy_types[type].danger
    if enemy_return is None:
        enemy_return = hero.findNearestEnemy()
    return enemy_return

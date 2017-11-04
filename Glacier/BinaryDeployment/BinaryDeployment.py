units = ['soldier', 'archer', 'griffin-rider']

for i in range(len(hero.findFriends())):
    result = ""
    unit = hero.findFriends()[i]
    if unit.type == "paladin":
        divide = 2
    else:
        divide = 3
    number = unit.deployment
    while number >= divide:
        a = number % divide
        number = (number - a) / divide
        result = a + result
    result = number + result

    while len(result) < 8:
        result = '0' + result

    for k in range(len(result)):
        m = result[k]
        hero.summon(units[m])
        hero.command(hero.built[len(hero.built) - 1], "move", {'x': 14 + k * 6, 'y': unit.pos.y})
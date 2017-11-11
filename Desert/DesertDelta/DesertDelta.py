# https://codecombat.com/play/level/desert-delta
# Only attack the enemies in the enemyNames array.
# Be sure to attack in order! 0 -> 1 -> 2 -> 3
enemyNames = ["Kog", "Godel", "Vorobun", "Rexxar"]

hero.attack(enemyNames[0])
hero.attack(enemyNames[1])
# Attack enemyNames[2]:
hero.attack(enemyNames[2])
# Attack the last element:
hero.attack(enemyNames[3])
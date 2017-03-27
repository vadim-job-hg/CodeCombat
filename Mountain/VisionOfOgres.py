# https://codecombat.com/play/level/vision-of-ogres
# Destroy a real ogre and illusions will disappear.

def findRealEnemy(enemies):
    for index in range(len(enemies)):
        enemy = enemies[index]
        # Convert the enemy's name (id) to lower case
        # and save it in a variable.
        lower = enemy.id.toLowerCase()
        # Split the name by whitespaces and save words.
        words = lower.split(' ')
        # Store the second word in a variable.
        second = words[1]
        # If the first letter of the second word equals to
        # the last letter of that word.
        if second[0] == second[len(second)-1]:
            # Then it's the real one. Return the enemy.
            return enemy

while True:
    ogres = hero.findEnemies()
    realOgre = findRealEnemy(ogres)
    if realOgre:
        while realOgre.health > 0:
            hero.attack(realOgre)

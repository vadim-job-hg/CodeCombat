#https://codecombat.com/play/level/alchemic-power
# Wait for alchemist's commands to fetch potions.

# The event handler for the pet's event "hear".
def waitFetch(event):
    # Find a nearest potion.
    potion = pet.findNearestByType("potion")
    # If the heard message is "Fetch":
    if event.message == 'Fetch':
        # Fetch the potion.
        pet.fetch(potion)
    # Else (for any other messages):
    else:
        # Return the pet to the red mark.
        pet.moveXY(54, 34)

pet.on("hear", waitFetch)

# You don't have to change code below.
while True:
    enemy = hero.findNearest(hero.findEnemies())
    if enemy:
        hero.attack(enemy)
    else:
        hero.moveXY(37, 34)

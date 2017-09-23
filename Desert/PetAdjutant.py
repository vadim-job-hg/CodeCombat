# https://codecombat.com/play/level/pet-adjutant
# Survive while wizards are casting to escape you.
# The medic and the cannon can help you.

# An event handler function for the pet.
def deliverCommand(event):
    # "event.message" contains the text that was said.
    # If somebody said "Fire":
    if event.message == "Fire":
        # Move the pet to the bottom mark.
        pet.moveXY(64, 16)
        # Make the pet say anything.
        pet.say('say')
        pass
    # If somebody said "Heal":
    elif event.message == "Heal":
        # Move the pet to the top mark.
        pet.moveXY(64, 52)
        # Make the pet say anything.
        pet.say('say')
        pass

pet.on("hear", deliverCommand)

# You haven't change the code below.
while True:
    enemy = hero.findNearestEnemy()
    if enemy:
        # If an enemy is too strong.
        if enemy.type == "brawler":
            hero.say("Fire")
        else:
            hero.attack(enemy)
    else:
        # If your hero needs medicine.
        if hero.health < hero.maxHealth / 2:
            hero.say("Heal")

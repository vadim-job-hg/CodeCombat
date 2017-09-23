# https://codecombat.com/play/level/pet-engineer
# Protect the camp from ogres.

# The event handler for the pet's event "hear".
def hearGuards(event):
    # Find guards to listen them.
    archer = pet.findNearestByType("archer")
    soldier = pet.findNearestByType("soldier")
    # If the speaker is the archer:
    if event.speaker == archer:
        # Move to the left button.
        pet.moveXY(32, 30)
    # If the speaker is the soldier:
    if event.speaker == soldier:
        # Move to the right button.
        pet.moveXY(48, 30)

pet.on("hear", hearGuards)

# You don't have to change code below.
# Your hero should protect the right bottom passage.
while True:
    enemy = hero.findNearestEnemy()
    if enemy:
        hero.attack(enemy)

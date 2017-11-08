# https://codecombat.com/play/level/guard-dog
# You can't help the peasants across the river.
# But, your pet can!
# Teach your wolf to be a guard dog.

def alarm(event):
    while True:
        # Pets can find enemies, too.
        enemy = pet.findNearestEnemy()
        # If there is an enemy:
        if(enemy):
            # Then have the pet say something:
            pet.say('Kavabanga')

pet.on("spawn", alarm);

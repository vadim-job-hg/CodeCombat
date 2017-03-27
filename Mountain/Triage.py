# https://codecombat.com/play/level/triage
# Triage the wounded soldiers.

doctor = hero.findByType("paladin")[0]
mage = hero.findByType("pixie")[0]
helper = hero.findByType("peasant")[0]
soldiers = hero.findByType("soldier")

# Initialize patient arrays.
doctorPatients = []
magePatients = []
helperPatients = []

# Iterate all the soldiers:
for soldier in soldiers:
    # If soldier is slowed:
    if soldier.maxSpeed < 6:
        # Add them to the mage's array of patients.
        magePatients.append(soldier)
    # Else if soldier.health is less than half of maxHealth:
    elif(soldier.maxHealth/2>soldier.health):
        # Add them to the doctor's array of patients.
        doctorPatients.append(soldier)
    # Else:
    else:
        # Add soldier to the helper's array of patients.
        helperPatients.append(soldier)

# Now assign the patient listss to the appropriate person.
mage["patients"] = magePatients
doctor["patients"] = doctorPatients
helper["patients"] = helperPatients

# https://codecombat.com/play/level/safety-blanket
# This is an array of nearby names!
# Enemies are at the 0, 2, 4, and 6 indexes of the array.
names = [
    "Thabt", "Victor", # 0, 1
    "Leerer", "Alianor", # 2, 3
    "Gorylo", "Millicent", # 4, 5
    "Weeb", "Brom", # 6, 7
]

# Attack the first two ogres at indexes 0 and 4.
hero.attack(names[0])
hero.attack(names[4])
# Attack the ogre at index 2:
hero.attack(names[2])
# Attack the ogre at index 6:
hero.attack(names[6])

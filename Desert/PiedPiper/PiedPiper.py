# https://codecombat.com/play/level/pied-piper

# Save hostages and escape.

# Put the pet close to the scouts.
pet.moveXY(24, 38)
# The shape shifting ability allows to lure ogres.
pet.shapeShift()
pet.moveXY(24, 6)
pet.moveXY(48, 6)

# Now lure brawlers to the sand yaks.
pet.moveXY(64, 40)
pet.shapeShift()
pet.moveXY(70, 19)
# The path is free and the hero can safely go home.
hero.moveXY(70, 60)

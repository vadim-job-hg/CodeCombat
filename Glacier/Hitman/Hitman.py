# https://codecombat.com/play/level/hitman
# Eliminate the Witch and don't let ogres see you.

# This function allows you to wait until an ability is ready.
def waitFor(abilityName):
    while True:
        if hero.isReady(abilityName):
            break

waitFor("phase-shift")
hero.phaseShift()
# Make sure that hero doesn't get stuck.
hero.moveXY(12, 62)
hero.moveXY(60, 62)
hero.moveXY(60, 56)

# Wait until "phase-shift" is ready, to use it: 
waitFor("phase-shift")
hero.phaseShift()
# Move to the next mark:
hero.moveXY(44, 17)

# Wait again, then use phaseShift and move:
waitFor("phase-shift")
hero.phaseShift()
hero.moveXY(6, 32)

# Wait, then use "phase-shift" to defeat the Witch with one hit:
waitFor("phase-shift")
hero.phaseShift()
hero.backstab("Yzzrith")


# http://codecombat.com/play/level/logical-path
# Get two secret true/false values from the wizard.
hero.moveXY(14, 24)
secretA = hero.findNearestFriend().getSecretA()
secretB = hero.findNearestFriend().getSecretB()

# If BOTH secretA and secretB are true, take the high path; otherwise, take the low path.
# Check the guide for notes on how to write logical expressions.
secretC = secretA and secretB
if secretC:
    hero.moveXY(20, 33)
else:
    hero.moveXY(20, 15)
hero.moveXY(26, 24)

# If EITHER secretA or secretB is true, take the high path.
secretC = secretA or secretB
if secretC:
    hero.moveXY(32, 33)
else:
    hero.moveXY(32, 15)
hero.moveXY(38, 24)

# Take the OPPOSITE of secretB and follow its path.
secretC = not secretB
if secretC:
    hero.moveXY(44, 33)
else:
    hero.moveXY(44, 15)
hero.moveXY(50, 24)

# https://codecombat.com/play/level/loud-quietness

# Get the volume and the password.

def onHear(event):
    # Get the volume and the password.
    words = event.message.split(" ")
    volume = words[0]
    password = words[1]
    # If the password should be loud:
    if volume == "Loud":
        # The pet says it in UPPER CASE.
        pet.say(words[1].toUpperCase())
    # If the password should be quiet:
    if volume == "Quiet":
        # The pet says it in lower case.
        pet.say(words[1].toLowerCase())
    pet.moveXY(pet.pos.x+ 24, pet.pos.y)

def passDoor():
    guard = hero.findNearest(hero.findFriends())
    password = guard.password
    # If the password should be loud:
    if guard.isLoud:
        # Say it in UPPER CASE.
        hero.say(password.toUpperCase())
        pass
    # If the password should be quiet:
    elif guard.isQuiet:
        # Say it in lower case.
        hero.say(password.toLowerCase())
        pass
    hero.moveXY(hero.pos.x+ 24, hero.pos.y)

# The pet can hear guards.
pet.on("hear", onHear)
# The hero should use their properties.
hero.moveXY(10, 14)
passDoor()
passDoor()

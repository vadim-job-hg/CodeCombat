# https://codecombat.com/play/level/double-agent

# Use the hidden number in the agent's message to escape.
# Count the number of trailing and leading whitespaces.

# This function return the coordinates of the n-th passage.
def passagePosByNum(n):
    return {"x": 60, "y": n * 12 + 8}

def onHear(event):
    # The original message.
    message = event.message
    # Trim the message.
    messages = message.trim(" ")
    # The hidden number is the difference of lengths.
    number = len(message)-len(messages);
    #for mess in messages:
    #    pet.say(mess)
    #    if mess==' ':
    #        number = number + 1
    pet.say(number)
    # Use passagePosByNum to find the passage enter.
    pos = passagePosByNum(number)
    # Move the pet to the enter of the passage.
    pet.moveXY(pos.x, pos.y)
    # Move the pet to the left edge of the map.
    pet.moveXY(0, pos.y)

pet.on("hear", onHear)

# The hero follows by the pet.The hero follows by the pet.
while True:
    hero.moveXY(pet.pos.x, pet.pos.y)


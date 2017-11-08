# https://codecombat.com/play/level/mightier-than-the-sword

# A variable is a way of holding on to a value.
# Here the "password" variable holds the secret phrase we need.
password = 'Secret Message'
hero.moveUp()
hero.moveRight()
hero.say(password)

# A variable changes its value whenever you assign it.
password = 'So Many Doors'
hero.moveRight()
hero.say(password)
# Change the string in this line to the password variable.
hero.say(password)  # Change this!
password = 'Let Me Out Of Here'
# Move to the last door and say the password variable to open it.
hero.moveRight()
hero.say(password)
hero.moveRight()

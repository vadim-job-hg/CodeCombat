# https://codecombat.com/play/level/the-wizards-door
# Move to Laszlo and get the secret number from him.
hero.moveXY(30, 13)
secret = hero.findNearestFriend().getSecret()
secretr = secret
number = secret + 7
# Follow Laszlo's instructions to get the magic number!
# Move to Erzsebet and say her magic number.
hero.moveXY(17, 26)
hero.say(number)
number = (7 + secret) % 4
# Move to Simonyi and say his magic number.
hero.moveXY(30, 39)
hero.say(number)
number = number * secretr
# Move to Agata and say her magic number.
hero.moveXY(43, 26)
hero.say(number)
# hero.say(number)

# http://codecombat.com/play/level/the-wizards-haunt
# Move to Zsofia and get the secret number from her.
hero.moveXY(18, 20)
secret = hero.findNearestFriend().getSecret()
number = secret / 4
# Follow Zsofia's instructions to get the magic number!
# Move to Mihaly and say his magic number.
hero.moveXY(30, 15)
hero.say(number)
# Move to Beata and say her magic number.
hero.moveXY(42, 20)
hero.say(number / 5)
number = number - number / 5
# Move to Sandor and say his magic number.
hero.moveXY(38, 37)
hero.say(number)

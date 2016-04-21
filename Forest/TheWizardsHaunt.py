#http://codecombat.com/play/level/the-wizards-haunt
# Move to Zsofia and get the secret number from her.
self.moveXY(18, 20)
secret = self.findNearestFriend().getSecret()
number = secret/4
# Follow Zsofia's instructions to get the magic number!
# Move to Mihaly and say his magic number.
self.moveXY(30, 15)
self.say(number)
# Move to Beata and say her magic number.
self.moveXY(42, 20)
self.say(number/5)
number = number - number/5
# Move to Sandor and say his magic number.
self.moveXY(38, 37)
self.say(number)

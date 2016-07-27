# http://codecombat.com/play/level/the-wizards-plane
# Move to Eszter and get the secret number from her.
self.moveXY(16, 32)
secret = self.findNearestFriend().getSecret()
num_thorn = secret
# Follow the instructions to get the magic number!
# Remember to use parentheses to do calculations in the right order.
# Move to Tamas and say his magic number.
num_doctor = num_thorn * 3 - 2
self.moveXY(24, 28)
self.say(num_doctor)
# Move to Zsofi and say her magic number.
num_bird = (num_doctor - 1) * 4
self.moveXY(32, 25)
self.say(num_bird)
# Move to Istvan and say his magic number.
num_hermes = (num_bird + num_doctor) / 2
self.moveXY(40, 21)
self.say(num_hermes)
# Move to Csilla and say her magic number.
num_purple = (num_doctor + num_bird) * (num_bird - num_hermes)
self.moveXY(48, 16)
self.say(num_purple)

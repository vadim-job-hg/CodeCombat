#http://codecombat.com/play/level/brawlwood

# This is the code for your base. Decide which unit to build each frame.
# Units you build will go into the self.built array.
# If you don't have enough gold, self.build() won't build anything.
# You start with 100 gold and receive 2 gold per second.
# Kill enemies, especially towers and brawlers, to earn more gold.
# Destroy the enemy base within 90 seconds!
# Check out the Guide just up and to the left for more info.

type = 'soldier'
if(self.built.length % 7 == 5):
    type = 'artillery'
elif(self.built.length % 4 == 1):
    type = 'archer'

#self.say('Unit #' + self.built.length + ' will be a ' + type)
self.build(type)

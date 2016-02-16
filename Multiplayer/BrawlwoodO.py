#http://codecombat.com/play/level/brawlwood?team=ogres
# This is the code for your base. Decide which unit to build each frame.
# Units you build will go into the self.built array.
# If you don't have enough gold, self.build() won't build anything.
# You start with 100 gold and receive 2 gold per second.
# Kill enemies, especially towers and brawlers, to earn more gold.
# Destroy the enemy base within 90 seconds!
# Check out the Guide just up and to the left for more info.

type = 'munchkin'
if self.built.length % 10 == 9:
    type = 'shaman'
elif self.built.length % 5 == 4:
    type = 'thrower'

#self.say('Unit #' + self.built.length + ' will be a ' + type)
self.build(type)

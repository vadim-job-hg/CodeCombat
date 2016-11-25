# http://codecombat.com/play/level/brawlwood?team=ogres
# This is the code for your base. Decide which unit to build each frame.
# Units you build will go into the hero.built array.
# If you don't have enough gold, hero.build() won't build anything.
# You start with 100 gold and receive 2 gold per second.
# Kill enemies, especially towers and brawlers, to earn more gold.
# Destroy the enemy base within 90 seconds!
# Check out the Guide just up and to the left for more info.

type = 'munchkin'
if hero.built.length % 10 == 9:
    type = 'shaman'
elif hero.built.length % 5 == 4:
    type = 'thrower'

# hero.say('Unit #' + hero.built.length + ' will be a ' + type)
hero.build(type)

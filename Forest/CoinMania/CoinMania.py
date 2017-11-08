# http://codecombat.com/play/level/coin-mania
# Each coin has a gold value associated with it, but we don't know how much.
# In such cases, we use while loop.
# Let's say I want to collect gold with total value 20.
# Here we use while loop, as we don't know how long the loop will run.

while hero.gold < 40:
    hero.moveRight()

hero.moveLeft()
hero.moveLeft()
while True:
    hero.attackNearbyEnemy()

# Now collect coins worth 40.
# If you want to kill the ogre, be careful as you will need atleast 70 health.
# Note: Mushrooms will decrease your health, which might even kill you.
# Write the while loop smartly.
# Your code here.

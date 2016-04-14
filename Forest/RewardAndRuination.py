#http://codecombat.com/play/level/reward-and-ruination
# It seems like the Ogre Chieftain is stealing your gems!
# Use the two artillery cannons to defeat your enemies and gather the gems.

while True:
    enemy = self.findNearestEnemy()
    if enemy:
        enemyPos = enemy.pos.x + " " + enemy.pos.y
        self.say("Enemy at " + enemyPos)

    # Now that you have sweet revenge, why not have your cake and eat it, too?
    # Find the item's position and say it for your artillery to target.
    #item = self.findNearestItem()
    item = self.findNearest(self.findItems())
    if item:
        itemPos = item.pos.x + " " + item.pos.y
        self.say("Enemy at " + itemPos)

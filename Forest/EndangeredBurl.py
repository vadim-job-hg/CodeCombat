loop:
enemy = self.findNearestEnemy()
if (enemy.type == "burl"):
    self.say("I'm not attacking that Burl!")
if ((enemy.type == "munchkin") or (enemy.type == "thrower")):
    self.attack(enemy)
if (enemy.type == "ogre"):
    self.moveXY(43, 49);

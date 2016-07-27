# You can use flags to choose different tactics.
# In this level, the green flag will mean you want to move to the flag.
# The black flag means you want to cleave at the flag.
# The doctor will heal you at the Red X

loop:
green = self.findFlag("green")
black = self.findFlag("black")
nearest = self.findNearestEnemy()
enemy = self.findNearestEnemy()
if enemy:
    dist = self.distanceTo(enemy);
if green:
    self.pickUpFlag(green)
elif black and self.isReady("cleave"):
    self.pickUpFlag(black)
    enemy = self.findNearestEnemy()
    if enemy:
        self.cleave(enemy);

elif nearest and self.distanceTo(nearest) < 10:
    self.attack(nearest)

    pass

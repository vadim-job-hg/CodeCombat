# http://codecombat.com/play/ladder/sky-span
# Tharin is a melee fighter with shield, warcry, and terrify skills.
# self.shield() lets him take one-third damage while defending.
# self.warcry() gives allies within 15m 40% haste for 5s, every 10s.
# self.powerUp() makes his next strike do 5x damage.
# self.terrify() sends foes within 30m fleeing for 5s, once per match.

friends = self.getFriends()
enemies = self.getEnemies()
if enemies.length is 0:
    return  # Chill if all enemies are dead.
enemy = self.getNearest(enemies)
friend = self.getNearest(friends)

# Which one do you do at any given time? Only the last called action happens.
# if not self.getCooldown("warcry"): self.warcry()
# if not self.getCooldown("terrify"): self.terrify()
# if not self.getCooldown("power-up") and not self.hasEffect('power-up'): self.powerUp()
# self.shield()
# self.attack(enemy)

# You can store state on self across frames:
# self.lastHealth = self.health

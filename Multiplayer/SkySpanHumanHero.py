# http://codecombat.com/play/ladder/sky-span
# Tharin is a melee fighter with shield, warcry, and terrify skills.
# hero.shield() lets him take one-third damage while defending.
# hero.warcry() gives allies within 15m 40% haste for 5s, every 10s.
# hero.powerUp() makes his next strike do 5x damage.
# hero.terrify() sends foes within 30m fleeing for 5s, once per match.

friends = hero.getFriends()
enemies = hero.getEnemies()
if enemies.length is 0:
    return  # Chill if all enemies are dead.
enemy = hero.getNearest(enemies)
friend = hero.getNearest(friends)

# Which one do you do at any given time? Only the last called action happens.
# if not hero.getCooldown("warcry"): hero.warcry()
# if not hero.getCooldown("terrify"): hero.terrify()
# if not hero.getCooldown("power-up") and not hero.hasEffect('power-up'): hero.powerUp()
# hero.shield()
# hero.attack(enemy)

# You can store state on self across frames:
# hero.lastHealth = hero.health

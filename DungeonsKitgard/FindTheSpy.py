# http://codecombat.com/play/level/find-the-spy?skip_protect_api=false
soldiers = self.getCombatants()

# Just killing the first soldier doesn't seem like a winning strategy...
# Click the "Guide" button if you need a hint on telling who is on what team.
for soldier in soldiers:
    spy = soldier
    if spy.team != 'humans':
        self.setTarget(spy)
        break
if spy and self.distanceTo(spy) > self.attackRange:
    self.setAction("move")
elif spy:
    self.setAction("attack")

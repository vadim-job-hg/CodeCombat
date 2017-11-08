# http://codecombat.com/play/level/find-the-spy?skip_protect_api=false
soldiers = hero.getCombatants()

# Just killing the first soldier doesn't seem like a winning strategy...
# Click the "Guide" button if you need a hint on telling who is on what team.
for soldier in soldiers:
    spy = soldier
    if spy.team != 'humans':
        hero.setTarget(spy)
        break
if spy and hero.distanceTo(spy) > hero.attackRange:
    hero.setAction("move")
elif spy:
    hero.setAction("attack")

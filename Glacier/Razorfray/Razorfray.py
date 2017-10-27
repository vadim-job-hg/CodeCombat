# https://codecombat.com/play/level/razorfray
# Use throwPos and removeFlag to throw where you aim flags.
# Kill ogres and the purple cow, but not the ice yak.
# Target placement is random with each submission.

while True:
    flag = hero.findFlag()
    if flag:
        hero.throwPos(flag.pos)
        hero.removeFlag(flag)

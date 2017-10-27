# http://codecombat.com/play/level/kelvintaph-pillars
# Move the stack of peasants onto another stump.
# You can only carry 1 peasant at a time.
# You cannot stack a larger peasant onto a smaller peasant.
# You have access to the following APIs:
# pickUpItem(container) picks up the top/last item in a container.
# dropItem(container) drops the top/last (and only) item in you're carrying.
# You and the stumps have the following APIs:
# peekItem() returns the top item of the container.
# viewStack() returns an array of items in the container.
# Peasants have the following APIs:
# size; returns the size of the peasant

stump1 = hero.findByType("stump")[0]  # This is where the peasants start.
stump2 = hero.findByType("stump")[1]
stump3 = hero.findByType("stump")[2]


def move(frm, to):
    hero.say(frm + '=>' + to)
    if frm == 2:
        hero.pickUpItem(stump1)
    elif frm == 1:
        hero.pickUpItem(stump2)
    else:
        hero.pickUpItem(stump3)

    if to == 2:
        hero.dropItem(stump1)
    elif to == 1:
        hero.dropItem(stump2)
    else:
        hero.dropItem(stump3)


def hanoi(n, frm, to, via):
    if (n == 1):
        move(frm, to)
        pass
    else:
        pass
        hanoi(n - 1, frm, via, to);
        move(frm, to)
        hanoi(n - 1, via, to, frm);


hanoi(5, 2, 3, 1)
# hero.pickUpItem(stump1)
# hero.dropItem(stump2)
# hero.say("Barrel 1 has the following peasants: " + stump1.viewStack())
# hero.say("Barrel 2's peasant is size: " + stump2.peekItem().size)

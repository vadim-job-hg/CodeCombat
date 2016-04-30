summonTypes = ['peasant']
def summonTroops():
    type = summonTypes[len(self.built)%len(summonTypes)]
    if self.gold > self.costOf(type):
        self.summon(type)

def commandPeasant(peasant):
    p = peasant
    c = p.findNearest(coins)
    n = p.findNearest(tails)
    if(len(tails)==0):
        hero.command(p, "move", c.pos)
        return

    me = Vector(p.pos.x,p.pos.y)

    co = Vector(c.pos.x,c.pos.y)

    go = Vector.subtract(co,me)
    go = Vector.normalize(go)


    if(p.distanceTo(n)<3.5):
        for j in range(0, len(tails)):
            e=tails[j]
            if(p.distanceTo(e)<3.5):
                he = Vector(e.pos.x,e.pos.y)
                eo = Vector.subtract(he,me)
                eo = Vector.normalize(eo)
                go = Vector.subtract(go,eo)

    go = Vector.add(go,me)
    hero.command(p, "move", go)

loop:
    friends = hero.findFriends()
    tails = hero.findEnemies()
    coins = hero.findItems()

    friends = self.findFriends()
    summonTroops()
    for friend in friends:
        commandPeasant(friend)




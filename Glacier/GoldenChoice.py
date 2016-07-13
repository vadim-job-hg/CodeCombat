#https://codecombat.com/play/level/golden-choice

################################################
'''
I Tried to finish this level  using recursion, but level to slow, when i Use it.

So I will finish level with most stupid way.

This is the example of recursion function(unfinished)

def CikleInCicle(y, k, summ):
    if y<9:
        summ = summ + goldMap[y][k]
        if k>0:
            summ1 = CikleInCicle(y+1, k - 1, summ)
        else:
            summ1 = 0
        if k<18:
            summ2 = CikleInCicle(y+1, k+1, summ)
        else:
            summ2 = 0
        #hero.say(y+'(y)'+k+'(k)'+summ1 +'x' +summ2)
        if summ1>summ2:
            return summ1 + summ
        else:
            return summ2 + summ
    else:
        #hero.say('top:' + goldMap[y][k])
        return goldMap[y][k]
goldMap = makeGoldMap(hero.findItems())
for kstart in range(0, 19, 2):
    summ = CikleInCicle(0, kstart, 0)
    #hero.say(kstart +'x' +summ)

Here I need to return the route with summ also, but i will newer do that, beacuse of message:

"Code never finished. It's either really slow or has an infinite loop."
'''
###############################################
kstart = []
for kstart[0] in range(0, 19, 2): #sorry for that
    for kstart[1] in range(1, 19, 2):#i am really sorry
        if Math.abs(kstart[0] - kstart[1]) == 1:
            for kstart[2] in range(0, 19, 2):#but i want to pass this level
                if Math.abs(kstart[1] - kstart[2]) == 1:
                    for kstart[3] in range(1, 19, 2):#the best code to slow
                        if Math.abs(kstart[2] - kstart[3]) == 1:
                            for kstart[4] in range(0, 19, 2):#i never do this again
                                if Math.abs(kstart[3] - kstart[4]) == 1:
                                    for kstart[5] in range(1, 19, 2):#thats such a shame
                                        if Math.abs(kstart[4] - kstart[5]) == 1:
                                            for kstart[6] in range(0, 19, 2):#i was drunk when i tipe it
                                                if Math.abs(kstart[5] - kstart[6]) == 1:
                                                    for kstart[7] in range(1, 19, 2):#realy realy
                                                        if Math.abs(kstart[6] - kstart[7]) == 1:
                                                            for kstart[8] in range(0, 19, 2):#I swear!
                                                                if Math.abs(kstart[7] - kstart[8]) == 1:
                                                                    for kstart[9] in range(1, 19, 2):#nex time i will use recursion
                                                                        if Math.abs(kstart[8] - kstart[9]) == 1:
                                                                            for y in range(0, 9):
                                                                                pass
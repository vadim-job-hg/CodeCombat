paladin = hero.findByType("paladin")[0]
minNum = 0
maxNum = paladin.maxNum
myBid = Math.floor((maxNum - minNum) / 2 + minNum)
while True:
    if paladin.pos.x == 40:
        minNum = 0
        maxNum = paladin.maxNum
        myBid = Math.floor((maxNum - minNum) / 2 + minNum)
    elif paladin.pos.x < 40:
        maxNum = myBid - 1
    else:
        minNum = myBid + 1
    myBid = Math.round(Math.random() * (maxNum - minNum) + minNum)
    hero.say(myBid)

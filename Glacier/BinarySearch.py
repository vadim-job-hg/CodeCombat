# http://codecombat.com/play/level/binary-search
# Guess the number that the paladin is thinking of each round.
# She will indicate whether the answer is a higher or lower number after each guess.
# She moves to x<39.5 if lower and x>40.5 if higher 
# and x==40 if correct.
# The paladin's maxNum property is the upper bound of the number.
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

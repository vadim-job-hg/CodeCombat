# https://codecombat.com/play/level/subarray-retreat?

# Find the subarray of gems with the best summary value.

# This function solves the problem in linear time.
def dynamicMaxSum (gems):
    cycles = 0
    maxStartIndex = 0
    maxEndIndex = 0
    maxEndHere = gems[0].value
    currentStartIndex = 0
    maxBest = 0
    for i in range(len(gems)):
        cycles += 1
        maxEndHere += gems[i].value
        if maxEndHere < 0:
            maxEndHere = 0
            currentStartIndex = i + 1
        if maxEndHere > maxBest:
            maxStartIndex = currentStartIndex
            maxEndIndex = i
            maxBest = maxEndHere
    hero.say("I's taken " + cycles + " cycles.")
    return [maxStartIndex, maxEndIndex]

# This function solves the problem in quadratic time.
def naiveMaxSum(gems):
    cycles = 0
    maxStartIndex = 0
    maxEndIndex = 0
    maxBest = 0
    for i in range(len(gems)):
        sum = 0
        for j in range(i, len(gems)):
            cycles += 1
            if cycles > 104:
                hero.say("I fed up of calculations.")
                return [i, j]
            sum += gems[j].value
            if sum > maxBest:
                maxStartIndex = i
                maxEndIndex = j
                maxBest = sum
    hero.say("I's taken " + cycles + " cycles.")
    return [maxStartIndex, maxEndIndex]

# Don't worry "findItems" sort out gems by X coordinate.
items = hero.findItems()
# Δ: Maybe we should change this function?
#edges = naiveMaxSum(items)
edges = dynamicMaxSum(items)

x1 = edges[0] * 4 + 4
x2 = edges[1] * 4 + 4

# Collect gems from x1 to x2 and escape:
hero.moveXY(x1, 40)
hero.moveXY(x2, 40)
hero.moveXY(40,64)

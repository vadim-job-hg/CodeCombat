# http://codecombat.com/play/level/gridmancer-redux
# Welcome to Gridmancer!
# A relic of days long past, the puzzle returns!
# Your task is to collect all the coins.
# You are given special methods to help with this task.
# this.addRect(x, y, w, h) places a rectangle to collect coins.
# this.removeRect(x, y) removes a previously added rectangle at the point.
# this.navGrid is (basically) a 2-dimensional array containing "Coin" or "Wall"
# You must collect all coins under rectangles
# Rectangles cannot collide with themselves or walls
# You need to make at most 55 rectangles to beat this level!
array_greed = hero.navGrid


def getRectngle(index1, index2):
    width = 0
    height = 0
    if array_greed[index1][index2] == 'Coin':
        indy = index2
        indx = index1
        for x in range(indx, lenght_xy):
            if array_greed[x][indy] == 'Coin':
                width = width + 1
            else:
                break
        for y in range(indy, lenght_xy):
            width_tmp = 0
            for x in range(indx, lenght_xy):
                width_tmp = width_tmp + 1
                # hero.debug(x+'_'+y+'_'+array_greed[x][y])
                if array_greed[x][y] != 'Coin':
                    return_object = {'x': index1, 'y': index2, 'width': width, 'height': height}
                    return return_object
                elif (width_tmp >= width):
                    height = height + 1
                    break
        return_object = {'x': index1, 'y': index2, 'width': width, 'height': height}
        return return_object
    else:
        return None
        # return {x:,y:,w:,h:}


rect = []  # {x, y, w, h}
lenght_xy = 20
for x in range(lenght_xy):
    for y in range(lenght_xy):
        rectg = getRectngle(x, y)
        if rectg:
            # hero.say([rectg.x, rectg.y, rectg.width, rectg.height])
            rect.push(rectg)
            for xi in range(rectg.x, rectg.x + rectg.width):
                for yi in range(rectg.y, rectg.y + rectg.height):
                    array_greed[xi][yi] = 'Got'
                    # hero.say(xi+'_'+yi+'_'+array_greed[xi][yi])
# hero.say(array_greed[0])
# hero.say([rect[0].x, rect[0].y, rect[0].width, rect[0].height])
index = 0
break_i = 56
for rec in rect:
    hero.addRect(rec.x, rec.y, rec.width, rec.height)
    if break_i == index:
        hero.say([rect[index].x, rect[index].y, rect[index].width, rect[index].height])
        break
    index = index + 1
# hero.addRect(0, 0, 4, 3)

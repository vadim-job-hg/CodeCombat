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
array_greed = self.navGrid
def getRectngle(cell, index1, index2):
    width = 1
    height = 1
    if cell=='Coin':
        indy = index1 + 1
        indx = index2
        while indy<len(array_greed):      
            if(array_greed[indy][indx]=='Coin'):
                height = height + 1
            else:
                break
            indy = indy + 1
            
        indx = indx + 1
        indy = index1
        while indx<len(array_greed[0]):
            tmp_height = 0;
            while indy<len(array_greed):      
                if(array_greed[indy][indx]!='Coin'):
                    break 2
                indy = indy + 1
            tmp_height = tmp_height + 1
            if tmp_height == height:
                width = width + 1
                break
            indx = indx + 1
        
        return {index1, index2, height, width}
    else:
        return None
  #return {x:,y:,w:,h:}
rect = []#{x, y, w, h}
for index1, row in enumerate(array_greed):
    for index2, cell in enumerate(row):
        rect = getRectngle(cell, index1, index2)
        if rect:
            self.say(rect);
#self.addRect(0, 18, 4, 2)
#self.addRect(0, 0, 4, 3)

#http://codecombat.com/play/level/gridmancer-redux
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
  
  return {x:,y:,w:,h:}
rect = []#{x, y, w, h}
for index1, row in enumerate(array_greed):
  for index2, cell in enumerate(row):
    self.say(getRectngle(cell, index1, index2))
#self.addRect(0, 18, 4, 2)
#self.addRect(0, 0, 4, 3)

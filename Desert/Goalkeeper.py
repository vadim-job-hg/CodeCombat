# Управляйте крестьянами, чтобы не позволить ограм забить гол.
# Тип огненного шара (файербол) - "ball"
def commandSoldiers(x, y):
    index = 0
    move = 0;
    for soldier in self.findFriends():
        if(index==1):
            xx = 18
            if x<60 and y<45:
                yy = y + 2
            else:
                yy = 42
        else:
            xx = 18
            if(x<30 and y>25):
                yy = y - 2
            else:                
                yy = 35
        self.command(soldier, "move", {'x':xx, 'y':yy})  
        index +=1
             
loop:  
    item = self.findNearest(self.findByType('ball'))
    if(item):
        commandSoldiers(item.pos.x, item.pos.y)

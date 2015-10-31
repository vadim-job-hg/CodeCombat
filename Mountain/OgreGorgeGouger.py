# У тебя только 20 секунд до прихода толпы огров!
# Хватай столько монет, сколько сможешь и уноси ноги на базу, закрывая проход за собой!
while self.now() < 30:
    item = self.findNearest(self.findItems())
    if item:
        if(self.isReady("jump") and self.distanceTo>15):
            self.jumpTo(item.pos)
        else:
            self.move(item.pos)
    if(self.gold>59):
        break
            
if(self.isReady("jump")):
    self.jumpTo({'x':21, 'y':38})
self.moveXY(21, 38)    
while self.pos.x > 16:
    self.move({'x':15, 'y':38})
self.buildXY('fence', 20, 38)

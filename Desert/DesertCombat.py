ordersGiven = 0
while ordersGiven < 5:
    x = self.pos.x
    y = self.pos.y - 10
    self.moveXY(x, y)
    # Перемещайся и отдавай приказы каждому из союзников. (Они тебя слышат только если ты стоишь напротив них.)
    self.say("Attack!")
    ordersGiven +=1;
    if(ordersGiven>=5):
        break;
self.moveXY(48, 31)
enemy = self.findNearestEnemy()
self.attack(enemy)
self.attack(enemy)
self.attack(enemy)
self.attack(enemy)
self.attack(enemy)
self.attack(enemy)
self.attack(enemy)
self.attack(enemy)
self.attack(enemy)
self.attack(enemy)
self.attack(enemy)
self.attack(enemy)
self.attack(enemy)


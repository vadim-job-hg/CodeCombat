# Find the treasure inside the maze.
# When you get the treasure, move to the exit.
# The exit is marked by the red cross. The level ends when you step on the mark.
# Some doors are blocked, some open when you are near them.

exitPosition = {"x": 150, "y": 120}
distanceBetweenRooms = 16
zeroShift = {"x": 10, "y": 10}
#http://codecombat.com/play/level/fragile-maze
distance = 16
move = Vector(0, -distance)
leftwall = Vector.rotate(move, Math.PI/2)
array_map = [[False,False,False,False,False,False,False,False,False,False],[False,False,False,False,False,False,False,False,False,False],[False,False,False,False,False,False,False,False,False,False],[False,False,False,False,False,False,False,False,False,False],[False,False,False,False,False,False,False,False,False,False],[False,False,False,False,False,False,False,False,False,False],[False,False,False,False,False,False,False,False,False,False],[False,False,False,False,False,False,False,False,False,False],[False,False,False,False,False,False,False,False,False,False],[False,False,False,False,False,False,False,False,False,False]]
x = 8
y = 6
stage = 1
while True:    
    direction = Vector.add(leftwall, hero.pos)    
    while not(hero.isPathClear(hero.pos, direction)):
        leftwall = Vector.rotate(leftwall, -Math.PI/2)
        direction = Vector.add(leftwall, hero.pos) 
    #hero.say(array_map[x][y])
    if array_map[x][y] != False:   
        hero.say(array_map[y][x])
        if array_map[x][y].x==leftwall.x and array_map[x][y].y==leftwall.y:
            hero.say('Already walk that way')
            #hero.say(array_map[y][x])
            leftwall = Vector.rotate(leftwall, -Math.PI)
            continue      
            pass
    
    #hero.say(leftwall)
    #hero.say(x+'x'+y)
    array_map[x][y] = {'x':leftwall.x, 'y':leftwall.y} 
    hero.moveXY(direction.x, direction.y) 
    if leftwall.x>1:
        x = x + 1
    elif leftwall.x<-1:
        x = x - 1
    if leftwall.y>1:
        y = y + 1
    elif leftwall.y<-1:
        y = y - 1
    leftwall = Vector.rotate(leftwall, Math.PI/2)



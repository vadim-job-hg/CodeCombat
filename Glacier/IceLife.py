# https://codecombat.com/play/level/ice-life
# You can define the inner field.
# 1 is a peasant, 0 is an empty cell.
innerField = [
        [1,1,1,0,0,0,0,0,0,0],
        [0,0,1,0,0,0,0,0,0,0],
        [0,1,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0],
        [0,1,0,0,0,0,0,0,0,0],
        [1,1,1,0,0,0,0,0,1,0],
        [0,0,1,0,0,0,0,1,0,0],
        [0,1,0,0,0,0,0,1,1,1]
        ]

hero.findNearestEnemy().initField(innerField)

while True:
    # It's to avoid infinity loop problem.
    hero.wait(60)

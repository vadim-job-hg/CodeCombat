game.spawnFloor("mountain")
game.setBounds("warp")
game.spawnDecorations("mountain", 19)

game.spawnRandomly("gem", 20, 19)
game.spawnRandomly("robobomb", 4, 105)

player = game.spawnPlayerXY('captain', 40, 34)
player.maxSpeed = 30

game.setPropertyFor("robobomb", "behavior", "AttacksNearest")

game.addCollectGoal(12)


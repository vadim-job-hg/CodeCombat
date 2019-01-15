# The program below creates the game shown at the left.
# In the game, the player moves the paddle to collect gems and defeat robots.
# Review the program. Can you see how each line of code makes part of the game?
# As you read, refer to the bank to learn what each method does.
# When you’re done, click “Run” to play the game the code creates!

# First, we create the walls and the floor:
game.spawnFloor("desert")
game.spawnLeftBorder("desert")
game.spawnRightBorder("desert")
game.spawnTopBorder("desert")

# Then, we create the movable paddle and set its speed:
game.spawnXY("glacier-platform", 40, 10)
game.setPropertyFor("glacier-platform", "speed", 50)

# We allow the paddle to collect items.
# Each item is worth 50 points.
game.setPropertyFor("glacier-platform", "collects", True)
game.setActionFor("glacier-platform", "collect", handler.addScore(50))

# We also set controls for the paddle.
# The 'A' key will make the paddle move left.
# The 'D' key will make it move right.
game.onInput("A", handler.moveLeft("glacier-platform"))
game.onInput("D", handler.moveRight("glacier-platform"))

# Now that the paddle is ready, we create the flying ball:
game.spawnXY("flying-ball", 40, 30)
game.setPropertyFor("flying-ball", "speed", 30)
game.setPropertyFor("flying-ball", "rotation", 0.8)

# When the ball hits things, it defeats them:
game.setActionFor("flying-ball", "collide", handler.defeatOther())

# If it leaves the screen, it comes back to the center:
game.setActionFor("flying-ball", "exit", handler.teleportTo(40, 40))

# Each lost ball costs 20 points:
game.setActionFor("flying-ball", "exit", handler.addScore(-20))

# Double-size robots score 100 points when defeated:
game.spawnXY("robobomb", 18, 52)
game.spawnXY("robobomb", 32, 52)
game.spawnXY("robobomb", 50, 52)
game.spawnXY("robobomb", 60, 48)
game.setPropertyFor("robobomb", "scale", 2)
game.setActionFor("robobomb", "defeat", handler.addScore(100))

# We also create invisible generators.
# They spawn gems in a 10-unit radius:
game.spawnXY("generator", 30, 58)
game.spawnXY("generator", 50, 58)
game.setPropertyFor("generator", "visible", False)
game.setPropertyFor("generator", "spawnType", "gem")
game.setPropertyFor("generator", "spawnRadius", 10)

# The gems should disappear when they leave the screen:
game.setPropertyFor("gem", "speed", 25)
game.setActionFor("gem", "update", handler.moveDown())
game.setActionFor("gem", "exit", handler.destroy())

# Lastly, we write the goal and directions for the players:
game.addDefeatGoal()
ui.setText("directions", "Use 'A' and 'D' keys to control the paddle.")
ui.setText("directions", "To win, defeat all the robots.")
ui.setText("directions", "Catch gems for bonus points.")

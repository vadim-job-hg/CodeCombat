# https://codecombat.com/play/level/how-much
# Calculate the perimeter and the area of the garden
# and pay the fair price for that.

# The prices for fences and lawns.
fencePrice = 3 # by one meter.
lawnPrice = 2 # by one square meter.
# You need the foreman.
foreman = hero.findNearest(hero.findFriends())
corners = foreman.corners
# Get the information about the garden.
bottomLeft = corners.bottomLeft
topRight = corners.topRight
# Calculate the size of the garden.
width = topRight.x - bottomLeft.x
height = topRight.y - bottomLeft.y
# Find the perimeter of the garden (meters).
perimeter = (width+height)*2
# Use fencePrice and calculate the fence cost.
fenceCost = fencePrice * perimeter
# Find the area of the garden (square metres).
area = width*height
# Use lawnPrice and calculate the lawn cost.
lawnCost = area * lawnPrice

# The total cost is the sum of the fence and the lawn costs
totalCost = fenceCost + lawnCost# Δ Calculate this.
hero.say("The total price is " + totalCost)
# Pay the bill.
foreman.bill(totalCost)

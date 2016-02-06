#http://codecombat.com/play/level/criss-cross?team=humans
# SUMMARY
#   * Your goal is to 'buy' a path of tiles from left to right.
#   * One group of tiles is available for bidding each turn.
#   * Each turn, bid to win one tile from the tile group.
#   * This code runs once a turn.

#############################################################################
# 1. Pick a tile from this turn's tileGroup to bid for.

# Here's a dumb but (relatively) simple strategy: try to buy a specific path.
# HINT: the default code for the other team is going for this path too!
coordinatesToBuy = [[0, 3], [1, 3], [2, 3], [3, 3], [4, 3], [5, 3], [6, 3]]

tiles = self.tileGroups[tileGroupLetter]  # tiles available this turn
tileIWant = None
for tile in tiles:
  if tile.owner: continue  # can't buy a tile that's been bought
  for coordinates in coordinatesToBuy:
    if coordinates[0] is not tile.x: continue
    if coordinates[1] is not tile.y: continue
    # We have a match!
    tileIWant = tile
    break
  if tileIWant: break

# If none of the tiles you want are available, skip this round
if not tileIWant: return None

#############################################################################
# 2. Choose your bid price. You only pay and win the tile if your bid wins.
myBid = Math.floor(5 + Math.random() * 10)

#############################################################################
# 3. Respond with an object with properties 'gold' and 'desiredTile'.

return {'gold': myBid, 'desiredTile': tileIWant}

# -- FOR MORE INFO, READ THE GUIDE -- #
#         It's at the top bar.

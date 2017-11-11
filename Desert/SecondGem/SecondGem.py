# https://codecombat.com/play/level/second-gem
# One gem is safe, others are bombs.
# But you know the answer: always take the second.

while True:
    items = hero.findItems()
    # If there are gems:
    if (len(items) > 1):
        # Collect the second from "items".
        hero.moveXY(items[1].pos.x, items[1].pos.y)
    # Else:
    else:
        # Move to the center mark.
        hero.moveXY(40, 34)


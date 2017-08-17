# https://codecombat.com/play/level/queue-manager
# Control the queue without mistakes.

# Useful string constants.
PHRASE_IN = " in"
PHRASE_OUT = " out"
IDLE = "idle"
# The list of workers.
workers = hero.findByType("peasant", hero.findFriends())
# Use this array to control the worker queue.
queue = []

while True:
    # Iterate all workers:
    for worker in workers:
        # If the worker's property "status" is "idle":
        if worker.status is IDLE:
            # Say the free worker's name with the word " in":
            hero.say(worker.id + PHRASE_IN)
            # Add the worker in the end of the queue:
            queue.append(worker)
    item = hero.findNearestItem()
    # If the item exists and the queue isn't empty:
    if item and len(queue)>0:
        # Say the name of the first in the queue worker
        # with the word " out":
        worker =  queue[0]
        hero.say(worker.id + PHRASE_OUT)
        # Remove (pop) the first one from the queue:
        queue.remove(worker)

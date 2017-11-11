# https://codecombat.com/play/level/teatime


def spawnMunchkins():
    munchkin1 = game.spawnXY("munchkin", 2, 12)
    munchkin2 = game.spawnXY("munchkin", 2, 56)
    munchkin1.behavior = "AttacksNearest"
    munchkin2.behavior = "AttacksNearest"


def spawnThrowers():
    thrower1 = game.spawnXY("thrower", 2, 24)
    thrower1.behavior = "AttacksNearest"
    thrower2 = game.spawnXY("thrower", 2, 44)
    thrower2.behavior = "AttacksNearest"


def spawnPotion():
    game.spawnXY("potion-large", 46, 34)


game.addSurviveGoal(30)

game.munshkinSpawnTime = 10
game.throwerSpawnTime = 10
game.potionSpawnTime = 5
game.nextPotionIn = 5

ui.track(game, "time")
ui.track(game, "nextPotionIn")

player = game.spawnHeroXY("duelist", 40, 34);
player.maxSpeed = 15


def updateTimers():
    if game.time > game.munshkinSpawnTime:
        spawnMunchkins()
        game.munshkinSpawnTime = game.munshkinSpawnTime + 3
    if game.time > game.throwerSpawnTime:
        spawnThrowers()
        game.throwerSpawnTime = game.throwerSpawnTime + 7
    if game.time > game.potionSpawnTime:
        spawnPotion()
        player.say("The potion is here!")
        game.potionSpawnTime = game.potionSpawnTime + 9
    game.nextPotionIn = game.potionSpawnTime - game.time


while True:
    updateTimers()

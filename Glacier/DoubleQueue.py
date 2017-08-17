# https://codecombat.com/play/level/double-queue

# Используй зелья для лечения солдат и мечи для вооружения крестьян.

# Просматривай очереди предметов и юнитов.
while True:
    item = hero.findNearestItem()
    unit = hero.findNearestFriend()
    if not item or not unit:
        continue
    # Используй свойство "type" для определения юнитов и предметов.
    # если предмет "potion", а юнит "soldier":
    if item.type == 'potion' and unit.type == "soldier":
        # Скажи имя юнита (`id`):
        hero.say(unit.id)
    # если предмет "sword", а юнит "peasant":
    elif item.type == 'sword' and unit.type == "peasant":
        # Скажи имя юнита (`id`):
        hero.say(unit.id)
    # Иначе скажи "Next".
    hero.say("Next")


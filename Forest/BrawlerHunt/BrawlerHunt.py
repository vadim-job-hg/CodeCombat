# https://codecombat.com/play/level/brawler-hunt
# Огры идут по одному.
# Не беспокойся по поводу мелких и средних огров.
# Твои цели - это драчуны (brawler)
# Подожди пока драчун достаточно близко (<50м) и прикажи стрелять.

while True:
    # Найди ближайшего врага и расстояние до него.
    enemy = hero.findNearestEnemy()
    # Если тип (type) огра равен "brawler" и расстояние до него меньше 50 метров.
    # Тогда скажи что угодно. Это будет сигнал для артиллерии, чтобы стрелять.
    if enemy  and enemy.type=='brawler' and hero.distanceTo(enemy)<50:
        hero.say('something')
    pass

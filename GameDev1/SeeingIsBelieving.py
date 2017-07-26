# https://codecombat.com/play/level/seeing-is-believing
# todo:
# Игроки любят видеть результат, используй `ui.track()`!
# Таким образом ты создашь элемент для отображения.
hero = game.spawnHeroXY(20, 20, "samurai")

spawner = game.spawnXY("generator", 50, 50)
spawner.spawnType = "munchkin"

# `ui.track() ` выводит пользователю свойство объекта.
ui.track(game, "time")

game.addSurviveGoal(20)

# Используй `ui.track`, чтобы отслеживать свойство "defeated":
ui.track(game, "defeated")
# Измени у героя `attack` и `maxSpeed`:
hero.attack = 20000
hero.maxSpeed = 50
# Добавь на поле боя точки создания врагов:
spawner2 = game.spawnXY("generator", 50, 50)
spawner2.spawnType = "munchkin"
# Начни играть и победи 10 манчкинов или скелетов!

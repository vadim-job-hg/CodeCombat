# http://codecombat.com/play/level/attack-wisely
# Избегите всех огненных ловушек
# Если вы ступите на огненную ловушку, то Вы будете взорваны
hero.moveUp();
hero.moveRight();
# hero.moveUp(); # Удалите эту линию
hero.moveRight();
hero.moveUp();
hero.moveRight(5);
enemy = hero.findNearestEnemy()
while enemy:
    hero.attack(enemy)
    enemy = hero.findNearestEnemy()
hero.moveUp(3);
hero.moveLeft();
hero.moveDown(3);
hero.moveLeft(2);
enemy = hero.findNearestEnemy()
while enemy:
    hero.attack(enemy)
    enemy = hero.findNearestEnemy()
hero.moveUp(2);
enemy = hero.findNearestEnemy()
while enemy:
    hero.attack(enemy)
    enemy = hero.findNearestEnemy()
hero.moveDown(2);
hero.moveLeft(2);
enemy = hero.findNearestEnemy()
while enemy:
    hero.attack(enemy)
    enemy = hero.findNearestEnemy()
hero.moveUp(2);
enemy = hero.findNearestEnemy()
while enemy:
    hero.attack(enemy)
    enemy = hero.findNearestEnemy()
hero.moveDown(3);
hero.moveLeft(2);
hero.moveUp();
enemy = hero.findNearestEnemy()
while enemy:
    hero.attack(enemy)
    enemy = hero.findNearestEnemy()
hero.moveUp(2);
enemy = hero.findNearestEnemy()
while enemy:
    hero.attack(enemy)
    enemy = hero.findNearestEnemy()
hero.moveDown(3);
hero.moveRight(2);
hero.moveDown();
# Подсказка 1: Чем больше враг, тем он сильнее
# Подсказка 2: Ты не должен убивать всех огров, если чувствуешь что недостаточно силен!


# Двигайтесь ближе к двери


# Атакуйте дверь при помощи команды "this.attack" ('DoorName')


# Заходите в комнату


# Attack the enemy inside the room (How to attack a no-named enemy ?)


# Move to gem alcove


# Атакуйте врагов


# Взять алмазы


# Now let's escape (move to the x-mark)
# Снова, избегите всех огненных ловушек

# http://codecombat.com/play/level/continuous-alchemy
# Обгони манчкинов в борьбе за воду, очищенную Omarn Brewstone.
# Ключевое слово `continue` - мощная штука для реализации сложной логики.
# Когда выполнение программы доходит до ключевого слова `continue`, оставшийся код цикла в текущей итерации будет пропущен.
# Однако, в отличии от ключевого слова `break`, выполнение цикла продолжится.
# Используй ключевое слово `continue` в проверке условий засады.
while True:
    # enemy = hero.findNearestEnemy()
    # item = hero.findNearestItem()
    enemy = hero.findNearestEnemy()
    item = hero.findNearestItem()
    # Если нет врага, продолжаем выйдя из этого витка цикла.
    if not enemy:
        continue

    # Если есть враг, но нет предмета, просим зелье и продолжаем выйдя из этого витка.
    if not item:
        hero.say("Дай мне попить!")
        continue

    # Используйте ключевое слово `if`, чтобы проверить тип (type) предмета. Если это яд ("poison"), продолжаем выйдя из этого витка.
    if item.type == 'poison':
        continue
    # Если нет, то зелье должно быть бутылкой воды, так что двигаемся к нему и возвращаемся обратно!
    hero.moveXY(item.pos.x, item.pos.y)
    hero.moveXY(34, 48)

# http://codecombat.com/play/level/storming-the-towers-of-areth
# The ogres are holed up in their camp
# Break through their defenses with a calculated strike!

hero.moveXY(55, 14)
hero.moveXY(92, 9)

# Установи мину ("fire-trap") на красном кресте.
hero.buildXY('fire-trap', 94, 19)
# Вернись к деревянному кресту чтобы не попасть под взрыв.
hero.moveXY(79, 6)
# Дождись пока солдат пойдет посмотреть на сверкающую мину.
# Проникни в лагерь и установи мины на каждом красном кресте.
hero.wait(5)
hero.moveXY(85, 34)
# Прикажи войскам отступать. (Подсказка: используй команду "say", "Retreat!")
hero.buildXY('fire-trap', 90, 53)
hero.buildXY('fire-trap', 60, 63)

hero.say("Retreat!")
# Беги к точке сбора, помеченной деревянным крестом в дальнем левом краю.
hero.moveXY(11, 28)

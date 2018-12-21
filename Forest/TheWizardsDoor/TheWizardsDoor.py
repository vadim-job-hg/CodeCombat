# Подойди к 'Laszlo' и узнай его секретное число.
hero.moveXY(30, 13)
las = hero.findNearestFriend().getSecret()

# Прибавь 7 к числу 'Laszlo', чтобы получить число 'Erzsebet'.
# Подойди к 'Erzsebet' и скажи её волшебное число.
erz = las + 7
hero.moveXY(17, 26)
hero.say(erz)
sim = erz/4
# Раздели число 'Erzsebet' на 4, чтобы получить число 'Simonyi'.
# Подойди к 'Simonyi'  и скажи его число.
hero.moveXY(30, 39)
hero.say(sim)
# Умножь число 'Simonyi' на число 'Laszlo', чтобы получить число 'Agata'.
# Подойди к 'Agata' и скажи её число.
hero.moveXY(43, 26)
hero.say(sim*las)

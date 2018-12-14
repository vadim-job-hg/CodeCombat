# Манчкины атакуют!
# Враги периодически атакуют группами.
# Если можешь, используй cleave, чтобы уничтожить толпу врагов.

while True:
    enemy = hero.findNearestEnemy()
    # Используй if с isReady, чтобы проверить "cleave":
    if (enemy and hero.isReady('cleave')):
        hero.cleave(enemy)
        # Руби! (cleave)
    # Если cleave еще не готова:
    else:
        hero.attack(enemy)
        # Атакуй ближайшего огра!

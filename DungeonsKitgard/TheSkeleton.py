#http://codecombat.com/play/level/the-skeleton
# Используйте loop для атаки скелета
# Тупой меч наносит мало урона, но далеко отбрасывает.
loop:
    enemy = hero.findNearestEnemy()
    hero.attack(enemy)

loop:
enemies = self.findEnemies()
enemyIndex = 0
while enemyIndex < len(enemies):
    enemy = enemies[enemyIndex]
    if enemy.type != "sand-yak" and enemy.health > 0:
        self.attack(enemy)
    enemyIndex += 1

//https://codecombat.com/play/level/javascript-back-to-back
// Оставайся по центру и защищай!

while(true) {
    var enemy = hero.findNearestEnemy();
    if (enemy) {
        // Или атакуй врага...
        hero.attack(enemy);
    }
    else {
        // ... или возвращайся назад на оборонительную позицию.
        hero.moveXY(40, 34);
    }
}


//https://codecombat.com/play/level/javascript-patrol-buster
// Помните, что врага в данный момент может не быть рядом.
while (true) {
    var enemy = hero.findNearestEnemy();
    if (enemy) {
        // Но когда он появится, атакуйте!
        hero.attack(enemy);
    }
}


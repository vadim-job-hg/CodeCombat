//https://codecombat.com/play/level/javascript-maniac-muchkins
while(true) {
    var enemy = hero.findNearestEnemy();
    var distance = hero.distanceTo(enemy);
    if (hero.isReady("cleave")) {
        hero.cleave(enemy);
    }
    else if (distance < 5) {
        hero.attack(enemy);
    }
    else {
        hero.attack('Chest');
    }
}




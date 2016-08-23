//https://codecombat.com/play/level/javascript-maniac-muchkins
while(true) {
    enemy = hero.findNearestEnemy();
    distance = hero.distanceTo(enemy);
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




//https://codecombat.com/play/level/army-training-2
// Defeat the ogres by spawning and commanding units.

// Spawn 2 "soldier"s.
game.spawnXY("soldier", 35, 20);
game.spawnXY("soldier", 45, 20);
// Spawn 2 "archer"s.
game.spawnXY("archer", 35, 20);
game.spawnXY("archer", 45, 20);
function fightEnemies(event) {
    while(true) {
        // event.target is the unit that is executing this event handler function!
        var friend = event.target;
        var enemy = friend.findNearestEnemy();
        // If there is an enemy
        if(enemy) {
        // Then have friend attack the enemy!
            friend.attack(enemy);
        }
    }
}

// This attaches the fightEnemies handler to all soldiers' "spawn" events.
game.setActionFor("soldier", "spawn", fightEnemies);

// Now, attach fightEnemies to the archers' "spawn" events:
game.setActionFor("archer", "spawn", fightEnemies);

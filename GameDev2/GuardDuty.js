//https://codecombat.com/play/level/guard-duty
// Add a soldier to the level to prevent ogres from crossing the path.
// Command the soldier using an event handler function.

function soldierLogic() {
    // Fill in the code for the soldier's actions here.
    // Remember to use 'soldier' instead of 'hero'!
    while(true) {
        var enemy = soldier.findNearestEnemy();
        // Attack the enemy, if the enemy exists.
        if(enemy)
            soldier.attack(enemy);
        // Else, move back to the starting position.
        else
            soldier.moveXY(42, 48);
    }

}

// This assigns your spawned unit to the soldier variable.
var soldier = game.spawnXY("soldier", 42, 48);
// This says to run the soldierLogic function when the soldier is spawned.
soldier.on("spawn", soldierLogic);

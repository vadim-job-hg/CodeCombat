//https://codecombat.com/play/level/javascript-return-to-thornbush-farm
// The function maybeBuildTrap defines TWO parameters!
function maybeBuildTrap(x, y) {
    // Use x and y as the coordinates to move to.
    hero.moveXY(x, y);
    var enemy = hero.findNearestEnemy();
    if(enemy) {
        // Use buildXY to build a "fire-trap" at the given x and y.
        hero.buildXY('fire-trap',x, y);
    }
}

while(true) {
    // This calls maybeBuildTrap, with the coordinates of the top entrance.
    maybeBuildTrap(43, 50);

    // Now use maybeBuildTrap at the left entrance!
    maybeBuildTrap(25, 34)
    // Now use maybeBuildTrap at the bottom entrance!
    maybeBuildTrap(43, 19)
}

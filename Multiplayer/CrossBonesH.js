//http://codecombat.com/play/level/cross-bones?team=humans
// Welcome to Cross Bones!
// Accumulate coins to raise a suitable army.
// Move to the X Markers to hire troops.
// Soldiers cost 20 gold to summon.
// Archers cost 25 gold to summon.
// If your hero has over a certain amount of gold, do something!
// Pick up the potion to heal yourself and the guardian.
// Watch for flags that may appear signaling certain events.
var go = false;
var attacked = false;
while (true) {
    var green = this.findFlag('green');
    var black = this.findFlag('black');
    var enemy = this.findNearestEnemy();
    if (black)
        attacked = true;
    if (green) {
        this.pickUpFlag(green);
    }
    if (this.now() > 75)
        go = true;
    if (((go) && this.gold >= 20) || this.gold >= 90 || attacked) {
        attacked = false;
        while (this.gold >= 20) {
            this.moveXY(58, 20);
            this.moveXY(58, 16);
        }
        if (green)
            this.pickUpFlag(green);
        if (go)
            this.moveXY(43, 37);

    } else if (go) {
        if (enemy && enemy.team == 'ogres') {
            if (this.isReady('power-up')) {
                this.powerUp();
                this.attack(enemy);
            } else
                this.attack(enemy);
        } else {
            this.moveXY(88, 74);
        }
    } else {
        var item = this.findNearestItem();
        if (item && item.type != "potion") {
            this.moveXY(item.pos.x, item.pos.y);
        }
    }
}

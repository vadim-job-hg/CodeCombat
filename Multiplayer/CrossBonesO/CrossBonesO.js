//http://codecombat.com/play/level/cross-bones?team=ogres
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
    if (((go) && this.gold >= 20) || this.gold >= 300) {
        attacked = false;
        while (this.gold >= 20) {
            this.moveXY(81, 99);
            this.moveXY(81, 103);
        }
        if (green)
            this.pickUpFlag(green);
        if (go)
            this.moveXY(91, 75);

    } else if (go) {
        if (enemy && enemy.team == 'ogres') {
            if (this.isReady('power-up')) {
                this.powerUp();
                this.attack(enemy);
            } else
                this.attack(enemy);
        } else {
            this.moveXY(20, 14);
        }
    } else {
        var item = this.findNearestItem();
        if (item && item.type != "potion") {
            this.moveXY(item.pos.x, item.pos.y);
        }
    }
}


//http://codecombat.com/play/ladder/dungeon-arena#ogres
this.attacksomeone = function (e, type) {
    if (!this.getCooldown('stomp') && type.indexOf('stomp') != -1) {
        this.stomp();
    } else if (!this.getCooldown('throw') && type.indexOf('throw') != -1) {
        this.throw(e);
    } else {
        this.attack(e);
    }
};
var nows = this.now();
var enemies = this.getEnemies();
if (enemies[1]) {
    this.attacksomeone(enemies[0], ['stomp', 'throw']);
}

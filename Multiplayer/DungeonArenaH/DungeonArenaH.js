//http://codecombat.com/play/ladder/dungeon-arena#humans
// Tharin is a melee fighter with shield, warcry, and terrify skills.
// this.shield() lets him take one-third damage while defending.
// this.warcry() gives allies within 10m 30% haste for 5s, every 10s.
// this.terrify() sends foes within 30m fleeing for 5s, once per match.

//http://codecombat.com/play/ladder/dungeon-arena#ogres
this.attacksomeone = function (e, type) {
    if (!this.getCooldown('warcry') && type.indexOf('warcry') != -1) {
        this.warcry();
    } else if (!this.getCooldown('terrify') && type.indexOf('terrify') != -1) {
        this.terrify(e);
    } else {
        this.attack(e);
    }
};
var nows = this.now();
var enemies = this.getEnemies();
if (enemies[1]) {
    this.attacksomeone(enemies[0], ['terrify', 'warcry']);
}


// Which one do you do at any given time? Only the last called action happens.
//if(!this.getCooldown('warcry')) this.warcry();
//if(!this.getCooldown('terrify')) this.terrify();
//this.shield();
//this.attack(enemy);

// You can also command your troops with this.say():
//this.say("Defend!", {targetPos: {x: 30, y: 30}});
//this.say("Attack!", {target: enemy});
//this.say("Move!", {targetPos: {x: 40, y: 40}});

// You can store state on this across frames:
//this.lastHealth = this.health;

// This code runs once per frame. Build units and command peons!
// Destroy the human base within 180 seconds.
// Run over 4000 statements per call and chooseAction will run less often.
// Check out the green Guide button at the top for more info.

var base = this;

/////// 1. Command peons to grab coins and gems. ///////
// You can only command peons, not fighting units.
// You win by gathering gold more efficiently to make a larger army.
// Click on a unit to see its API.
var items = base.getItems();
var peons = base.getByType('peon');
for (var peonIndex = 0; peonIndex < peons.length; peonIndex++) {
    var peon = peons[peonIndex];
    var item = base.getNearest(items);
    if (item)
        base.command(peon, 'move', items[0].pos);
}


/////// 2. Decide which unit to build this frame. ///////
// Peons can gather gold; other units auto-attack the enemy base.
// You can only build one unit per frame, if you have enough gold.
var type;
if (base.built.length === 0) {
    type = 'peon';
    if (base.gold >= base.buildables[type].goldCost)
        base.build(type);
}
else {
    type = ['peon', 'ogre', 'munchkin', 'brawler', 'ogre', 'ogre', 'fangrider', 'fangrider', 'brawler', 'shaman', 'munchkin', 'munchkin', 'munchkin', 'munchkin'];
    /*if(typeof(index) != 'numeric')
     index =0;
     else index++;*/
    if (base.gold >= base.buildables[type[base.built.length % type.length]].goldCost)
        base.build(type[base.built.length % type.length]);
}


// 'peon': Peons gather gold and do not fight.
// 'munchkin': Light melee unit.
// 'ogre': Heavy melee unit.
// 'shaman': Support spellcaster.
// 'fangrider': High damage ranged attacker.
// 'brawler': Mythically expensive super melee unit.
// See the buildables documentation below for costs and the guide for more info.

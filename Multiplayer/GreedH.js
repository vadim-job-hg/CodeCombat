//http://codecombat.com/play/level/greed
// This code runs once per frame. Build units and command peasants!
// Destroy the ogre base within 180 seconds.
// Run over 4000 statements per call and chooseAction will run less often.
// Check out the green Guide button at the top for more info.

var base = this;

/////// 1. Command peasants to grab coins and gems. ///////
// You can only command peasants, not fighting units.
// You win by gathering gold more efficiently to make a larger army.
// Click on a unit to see its API.
var items = base.getItems();
var peasants = base.getByType('peasant');
for (var peasantIndex = 0; peasantIndex < peasants.length; peasantIndex++) {
    var peasant = peasants[peasantIndex];
    var item = peasant.getNearest(items);
    if (item)
        base.command(peasant, 'move', item.pos);
}


/////// 2. Decide which unit to build this frame. ///////
// Peasants can gather gold; other units auto-attack the enemy base.
// You can only build one unit per frame, if you have enough gold.
var type;
if (base.built.length === 0) {
    type = 'peasant';
    if (base.gold >= base.buildables[type].goldCost)
        base.build(type);
}
else {
    type = ['peasant', 'knight', 'griffin-rider', 'griffin-rider', 'knight', 'knight', 'soldier', 'librarian', 'griffin-rider', 'captain'];
    /*if(typeof(index) != 'numeric')
     index =0;
     else index++;*/
    if (base.gold >= base.buildables[type[base.built.length % type.length]].goldCost)
        base.build(type[base.built.length % type.length]);
}


// 'peasant': Peasants gather gold and do not fight.
// 'soldier': Light melee unit.
// 'knight': Heavy melee unit.
// 'librarian': Support spellcaster.
// 'griffin-rider': High-damage ranged attacker.
// 'captain': Mythically expensive super melee unit.
// See the buildables documentation below for costs and the guide for stats.

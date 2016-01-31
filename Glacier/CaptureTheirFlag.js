//http://codecombat.com/play/level/capture-their-flag?team=humans
this.moveTo =  function (position){
    var distance = 30;
    var  goalf = position;
    missile = this.findNearest(this.findEnemyMissiles());
    if(missile && this.distanceTo(missile) < distance){
        vectorToH = Vector.subtract(this.pos, missile.pos);
        vectorToH = Vector.normalize(vectorToH);
        vectorToH = Vector.multiply(vectorToH, distance);
        goalf =  Vector.add(vectorToH, goalf);
    }
    if(this.isReady("jump"))
        this.jumpTo(goalf);
    else
        this.move(goalf);
};
this.commandTroops =  function(){
    var friends = this.findFriends();
    for(var index in friends){
        if(friends[index].type == 'robot-walker')
            this.CommandRobot(friends[index]);
        else if(friends[index].type == 'soldier')
            this.CommandSoldier(friends[index]);
    }
};
this.CommandRobot =  function(friend){
   target = friend.findNearestEnemy();
    if(target)
        this.command(friend, "attack", target);
};
this.CommandSoldier =  function(friend){
       target = friend.findNearestEnemy();
    if(target)
        this.command(friend, "attack", target);
};

this.summonTroops = function(){
    vartype = 'soldier';
    if(this.gold > this.costOf(type))
        this.summon(type);
};
this.placeFlag({'x':20, 'y':60});
this.placeFlag({'x':-6, 'y':109});
this.placeFlag({'x':-7, 'y':9});
var target;
var captured = false;
loop {
    flags = this.findByType('flag');
    for(var i in flags){
        if(flags[i].team=='ogres' && flags[i].pos.x>70){
            target = flags[i];
            break;
        }
    }
    if(target && this.distanceTo(target)<3 && !captured){
         flag = this.findEnemyFlags();
         this.captureFlag(flag[0]);
         captured = true;
     }
    else if(target && this.distanceTo(target)>3 && !captured){
         this.moveTo(target.pos);
    } else if(captured)  {
         this.moveTo({'x':65, 'y':this.pos.y});
         if(this.pos.x<=67){
                captured = false;
        }
    }
    //this.summonTroops();
    this.commandTroops();
}

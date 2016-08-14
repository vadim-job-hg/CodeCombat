// For this level you will have 3 main functions that you need to use.
// placeFlag - this should be called three times at the beginning of your code to hide your 3 flags
// findEnemyFlags - this should be called in order to locate enemy flags, it returns an array of any enemy flag within 5 units of you
// captureFlag - this is called on a flag you've found and captures it if you are within 3 units of the flag, then you can run the flag back to your side of the map
// you also have the ability to control your robot-walker, though he can only fire, not move
this.moveTo =  function (position){
    var distance = 30;
    var  goalf = position;
    missile = this.findNearest(this.findEnemyMissiles());
    if(typeof missile!='undefined' && this.distanceTo(missile) < distance){
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
this.placeFlag({'x':120, 'y':63});
this.placeFlag({'x':160, 'y':109});
this.placeFlag({'x':160, 'y':9});
var target;
var captured = false;
loop {
    var flags = '';
    flags = this.findByType('flag');
    for(var i in flags){
        if(flags[i].team=='humans' && flags[i].pos.x<70){
            target = flags[i];
            break;
        }
    }
    //hero.say(target);
    if(typeof target!='undefined' && this.distanceTo(target)<3 && !captured){
         var flag = this.findEnemyFlags();
         this.captureFlag(flag[0]);
         captured = true;
     }
    else if(typeof target!='undefined' &&  this.distanceTo(target)>3 && !captured){
         //this.moveTo(target.pos);
         this.move(target.pos);
    } else if(captured)  {
         this.move({'x':74, 'y':this.now()});
         if(this.pos.x>=74){
                captured = false;
        }
    }
    //this.summonTroops();
    this.commandTroops();
}


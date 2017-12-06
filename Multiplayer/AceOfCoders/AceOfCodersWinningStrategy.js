/* eslint no-unused-vars:0 */
/* global enumerate */

function filterType(type, arr) {
    var newArr = [];
    for (let item of arr) {
        if (item.type === type) {
            newArr.push(item);
        }
    }

    return newArr;
}

function removeType(type, arr) {
    var newArr = [];
    for (let item of arr) {
        if (item.type !== type) {
            newArr.push(item);
        }
    }

    return newArr;
}

function firstOfType(type, arr) {
    for (let ent of arr) {
        if (ent.type === type) {
            return ent;
        }
    }

    return null;
}

function findNearestTo(pos, arr) {
    var winner = null;
    var winDistance = Infinity;

    for (let item of arr) {
        var distance = pos.distance(item.pos);
        if (distance < winDistance) {
            winner = item;
            winDistance = distance;
        }
    }

    return winner;
}

function findNearestToIndexed(pos, arr) {
    var winIndex = -1;
    var winDistance = Infinity;

    for (let [i, item] of enumerate(arr)) {
        var distance = pos.distance(item.pos);
        if (distance < winDistance) {
            winIndex = i;
            winDistance = distance;
        }
    }

    return winIndex;
}

function findNearestTargetPosTo(pos, arr) {
    var winner = null;
    var winDistance = Infinity;

    for (let item of arr) {
        var distance = pos.distance(item.targetPos);
        if (distance < winDistance) {
            winner = item;
            winDistance = distance;
        }
    }

    return winner;
}

function findInRadiusOfUnit(unit, radius, arr) {
    var items = [];
    for (let item of arr) {
        if (unit.distanceTo(item) < radius) {
            items.push(item);
        }
    }

    return items;
}

function findInRadiusOfPosition(pos, radius, arr) {
    var items = [];
    for (let item of arr) {
        if (pos.distance(item.pos) < radius) {
            items.push(item);
        }
    }

    return items;
}

function firstInRadiusOfPosition(pos, radius, arr) {
    for (let item of arr) {
        if (pos.distance(item.pos) < radius) {
            return item;
        }
    }

    return null;
}

function findLowestHealth(units) {
    var winner = null;
    var winScore = Infinity;
    for (let u of units) {
        var score = u.health;
        if (score < winScore) {
            winner = u;
            winScore = score;
        }
    }

    return winner;
}

function findLowestHealthNearest(unit, units) {
    var winner = null;
    var winHealth = Infinity;
    var winDistance = Infinity;
    for (let u of units) {
        var health = u.health;
        var distance = unit.pos.distance(u.pos);

        if (health < winHealth) {
            winner = u;
            winHealth = health;
            winDistance = distance;
        }
        else if (health === winHealth) {
            if (distance < winDistance) {
                winner = u;
                winHealth = health;
                winDistance = distance;
            }
        }
    }

    return winner;
}

this.filterFriends = function(arr) {
    var newArr = [];
    for (let item of arr) {
        if (item.team === this.team) {
            newArr.push(item);
        }
    }

    return newArr;
};

this.filterEnemies = function(arr) {
    var newArr = [];
    for (let item of arr) {
        if (item.team === this.team) {
            newArr.push(item);
        }
    }

    return newArr;
};

this.findInRadius = function(radius, arr) {
    var items = [];

    for (let item of arr) {
        if (this.distanceTo(item) < radius) {
            items.push(item);
        }
    }

    return items;
};
/*
global
Vector
firstOfType
findNearestTo
findInRadiusOfUnit
findInRadiusOfPosition
findNearestTargetPosTo
firstInRadiusOfPosition
findLowestHealthNearest
removeType
*/

// constants

/* eslint-disable no-unused-vars */
const SOLDIER_RANGE = 3;
const ARCHER_RANGE = 25;
const ARTILLERY_RANGE = 65;
const ARROW_TOWER_RANGE = 30;
const GOLIATH_RANGE = 5;

const GOLIATH_TYPE = "goliath";
const SOLDIER_TYPE = "soldier";
const ARCHER_TYPE = "archer";
const TOWER_TYPE = "arrow-tower";
const ARTILLERY_TYPE = "artillery";
const SHELL_TYPE = "shell";
const BOULDER_TYPE = "boulder";
const ARROW_TYPE = "arrow";
const YAK_TYPE = "ice-yak";
/* eslint-enable no-unused-vars */

// utility functions -----------------------------------------------------------

// Computes the total value of combat units
function valuateFighters(units) {
    var sum = 0;
    for (let u of units) {
        sum += valuateFighter(u);
    }

    return sum;
}

function valuateFighter(u) {
    switch (u.type) {
        case SOLDIER_TYPE:
            return 20;
        case ARCHER_TYPE:
            return 25;
        case ARTILLERY_TYPE:
            return 75;
        case TOWER_TYPE:
            return 100;
        case GOLIATH_TYPE:
            return 500;
        default:
            return 0;
    }
}

// unit selection --------------------------------------------------------------

var emergArtyBuiltTime = -Infinity;
this.chooseUnitToBuild = function() {
    // it's not a good idea to build units
    // while on the wrong side of the map
    // and on the wrong side of the enemy goliath
    var farPos = pointsMap.farCorner.pos;
    var nearPos = pointsMap.nearCorner.pos;
    var farDistance = this.pos.distance(farPos);
    var nearDistance = this.pos.distance(nearPos);

    // positive value means closer to enemy base than home base.
    // negative value means closer to home base than enemy base.
    // 0 is equidistant.
    var distanceDelta = nearDistance - farDistance;

    // if we're almost closer to the enemy side,
    // and the enemy goliath is behind us,
    // inhibit spawning.
    if (distanceDelta > -10 && goliath.pos.distance(farPos) >= farDistance) {
        return null;
    }

    var artillery = this.findByType(ARTILLERY_TYPE, friends);

    // if we are under fire,
    // and our artillery can't get into range,
    // build an emergency artillery
    var nearestEnemyArtillery = this.findNearest(enemyArtillery);
    if (nearestEnemyArtillery) {
        var friendlyArtillery = findNearestTo(nearestEnemyArtillery.pos, artillery);
        var friendlyArtilleryDistance = Infinity;
        if (friendlyArtillery) {
            friendlyArtilleryDistance = nearestEnemyArtillery.pos.distance(friendlyArtillery.pos);
        }
        if (this.gold > 75 && this.gold > goliath.gold * 3
                && this.distanceTo(nearestEnemyArtillery) <= ARTILLERY_RANGE
                && friendlyArtilleryDistance > ARTILLERY_RANGE + 20
                && this.now() - emergArtyBuiltTime > 3) {
            emergArtyBuiltTime = this.now();
            return ARTILLERY_TYPE;
        }
    }

    // suppress spawning when in range of shells
    var shell = this.findNearest(shells);
    if (shell && this.pos.distance(shell.targetPos) < 20) {
        return null;
    }
    var boulder = this.findNearest(boulders);
    if (boulder && this.pos.distance(boulder.targetPos) < 15) {
        return null;
    }

    // inhibit spawning if archers are in range
    // and we haven't recently thrown a rock at them
    var nearestEnemyArcher = this.findNearest(enemyArchers);
    if (nearestEnemyArcher
            && this.distanceTo(nearestEnemyArcher) <= ARCHER_RANGE
            && this.now() - throwArcherTime > 1) {
        return null;
    }

    var archers = this.findByType(ARCHER_TYPE, friends);

    if (this.now() < 5 && artillery.length < 1) {
        return ARTILLERY_TYPE;
    }

    // if we already have an army,
    // and the enemy has artillery, but we don't,
    // build an artillery
    if (this.now() > 5
            && enemyArtillery.length > 0
            && artillery.length === 0
            && archers.length >= 5) {
        return ARTILLERY_TYPE;
    }

    // if the enemy is hanging back with siege, make sure we have an artillery
    var siegeCount = enemyTowers.length + enemyArtillery.length;
    var armyCount =
        enemyTowers.length +
        enemyArtillery.length +
        enemyArchers.length +
        enemySoldiers.length;

    if (this.now() > 5
            && pointsMap.center.team === this.team
            && siegeCount/armyCount > 0.33
            && artillery.length === 0
            && this.distanceTo(goliath) > 10) {
        return ARTILLERY_TYPE;
    }

    return ARCHER_TYPE;
};

this.chooseStructureToBuild = function() {
    if (friends.length < 5) {
        return null;
    }
    var point = this.findNearest(this.getControlPoints());

    // don't build towers while enemy artillery lives,
    // it's a waste.
    if (enemyArtillery.length > 0) {
        return null;
    }

    // suppress spawning when in range of shells
    var shell = this.findNearest(shells);
    if (shell && this.pos.distance(shell.targetPos) < 20) {
        return null;
    }

    // build a tower on the nearest point if we're close enough
    // and enemy archers are threatening it
    var archersNearPoint = findInRadiusOfPosition(point.pos, 30, enemyArchers);
    if (archersNearPoint > 2 && this.pos.distance(point.pos) <= 20) {
        var tower = findNearestTo(point.pos, this.findByType(TOWER_TYPE, friends));
        if (!tower || tower.pos.distance(point.pos) > 20) {
            return { structure: TOWER_TYPE, pos: new Vector(this.pos.x - buildOffsetX, this.pos.y - buildOffsetY) };
        }
    }

    return null;
};

this.buildArmy = function() {
    var struct = this.chooseStructureToBuild();
    if (struct) {
        if (this.gold >= this.costOf(struct.structure)) {
            this.buildXY(struct.structure, struct.pos.x, struct.pos.y);
            return 1;
        }
    }
    else {
        var type = this.chooseUnitToBuild();
        if (type && this.gold >= this.costOf(type)) {
            this.buildXY(type, this.pos.x - buildOffsetX, this.pos.y - buildOffsetY);
            return 1;
        }
    }

    return 0;
};


// unit objective allocation ---------------------------------------------------

this.computeEnemyStrength = function(point) {
    var units = findInRadiusOfPosition(point.pos, 20, enemies);
    var strength = valuateFighters(units);
    return strength;
};

this.allocateAndCommandBasic = function() {
    var archers = this.findByType(ARCHER_TYPE, friends);
    var pA = pointsMap.nearA;
    var archerA = findNearestTo(pA.pos, archers);

    var pB = pointsMap.nearB;
    var archerB = findNearestTo(pB.pos, archers);

    if (archerA) {
        this.archerBasic(archerA, pA);
    }
    if (archerB) {
        this.archerBasic(archerB, pB);
    }

    if (archerA && archerB && archerA.id === archerB.id) {
        if (archerA.pos.distance(pA.pos) < archerA.pos.distance(pB.pos)) {
            this.archerBasic(archerA, pA);
        }
        else {
            this.archerBasic(archerA, pB);
        }
    }

    var center = pointsMap.center;
    var centerCaptured = center.team === this.team;

    var a;
    if (!centerCaptured || this.now() <= 8) {
        for (a of archers) {
            if (a.id === archerA.id) {
                continue;
            }
            if (a.id === archerB.id) {
                continue;
            }
            this.archerBasic(a, center);
        }
    }
    else {
        var archerCenter = findNearestTo(center.pos, archers);
        for (a of archers) {
            if (a.id === archerA.id) {
                continue;
            }
            if (a.id === archerB.id) {
                continue;
            }
            if (a.id === archerCenter.id) {
                this.archerBasic(archerCenter, center);
                continue;
            }

            this.archerBasic(a, null);
        }
    }
};

// unit control ----------------------------------------------------------------

this.commandTower = function(unit) {
    var targets = findInRadiusOfUnit(unit, ARROW_TOWER_RANGE, enemies);
    var target = findLowestHealthNearest(unit, targets);
    if (target) {
        this.command(unit, "attack", target);
    }
};

this.commandArtillery = function(unit) {

    // attack artillery in range
    var nearestArtillery = findNearestTo(unit.pos, enemyArtillery);
    if (nearestArtillery) {
        var artilleryDistance = unit.pos.distance(nearestArtillery.pos);
        if (artilleryDistance <= ARTILLERY_RANGE) {
            this.command(unit, "attack", nearestArtillery);
            return;
        }
        else if (artilleryDistance <= ARTILLERY_RANGE + 10) {
            this.command(unit, "attackPos", Vector.add(unit.pos, Vector.multiply(Vector.normalize(Vector.subtract(nearestArtillery.pos, unit.pos)), ARTILLERY_RANGE)));
            return;
        }
    }
    else if (this.now() < 4 && goliath.gold < 75) {
        this.command(unit, "attackPos", new Vector(goliath.pos.x - (buildOffsetX*2), goliath.pos.y - (buildOffsetY*2)));
        return;
    }

    // attack towers in range
    var nearestTower = findNearestTo(unit.pos, enemyTowers);
    if (nearestTower
            && unit.pos.distance(nearestTower.pos) <= ARTILLERY_RANGE) {
        this.command(unit, "attack", nearestTower);
        return;
    }

    // kite nearby enemies
    var nearestEnemy = findNearestTo(unit.pos, enemies);
    if (unit.pos.distance(nearestEnemy.pos) <= 35) {
        var dir = Vector.normalize(
                Vector.subtract(unit.pos, nearestEnemy.pos));

        this.command(unit, "move", Vector.add(
                    unit.pos,
                    Vector.multiply(dir, 10)));
        return;
    }

    // dodge shells
    var nearestShell = findNearestTo(unit.pos, shells);
    if (nearestShell && nearestShell.targetPos.distance(unit.pos) <= 15) {
        var shellDir = Vector.normalize(
                Vector.subtract(unit.pos, nearestShell.targetPos));
        if (shellDir.magnitude() < 0.8) {
            this.command(unit, "move", pointsMap.nearCorner.pos);
            return;
        }
        this.command(unit, "move", Vector.add(
                    unit.pos,
                    Vector.multiply(shellDir, 10)));
        return;
    }

    // attack artillery, regardless of range
    if (nearestArtillery) {
        var goVec = new Vector(0, 0);
        var nearArtyDir = Vector.normalize(Vector.subtract(nearestArtillery.pos, unit.pos));
        goVec = Vector.add(goVec, Vector.multiply(nearArtyDir, 1));

        for (let en of enemies) {
            if (en.id === nearestArtillery.id) {
                continue;
            }
            var enDist = en.pos.distance(unit.pos);
            if (enDist > 40) {
                continue;
            }
            var enDir = Vector.normalize(Vector.subtract(unit.pos, en.pos));
            goVec = Vector.add(goVec, Vector.multiply(enDir, (36*36)/(enDist * enDist)));
        }
        var topDist = 95 - unit.pos.y;
        var botDist = unit.pos.y;
        var leftDist = unit.pos.x;
        var rightDist = 115 - unit.pos.x;
        goVec = Vector.add(goVec, new Vector(0, -100/(topDist * topDist)));
        goVec = Vector.add(goVec, new Vector(0, 100/(botDist * botDist)));
        goVec = Vector.add(goVec, new Vector(100/(leftDist * leftDist), 0));
        goVec = Vector.add(goVec, new Vector(-100/(rightDist * rightDist), 0));

        var movePos = Vector.add(unit.pos, Vector.multiply(Vector.normalize(goVec), 10));

        this.command(unit, "move", movePos);
        return;
    }

    // attack enemy points
    var farA = pointsMap.farA;
    var farB = pointsMap.farB;
    var siegePoint = null;
    if (farA.team && farA.team !== this.team) {
        if (farB.team && farB.team !== this.team) {
            if (unit.pos.distance(farA.pos) < unit.pos.distance(farB.pos)) {
                siegePoint = farA;
            }
            else {
                siegePoint = farB;
            }
        }
        else {
            siegePoint = farA;
        }
    }
    else if (farB.team && farB.team !== this.team) {
        siegePoint = farB;
    }
    if (siegePoint) {
        this.command(unit, "attackPos", siegePoint.pos);
        return;
    }

    // attack towers, regardless of range
    if (nearestTower) {
        this.command(unit, "attack", nearestTower);
        return;
    }

    // then goliath
    this.command(unit, "attack", goliath);
};

this.archerBasic = function(unit, defendPoint) {
    var threats = [];

    // figure out the threats

    // avoid the splash of artillery shells
    var shell = findNearestTargetPosTo(unit.pos, shells);
    if (this.now() > 5 && shell && shell.targetPos.distance(unit.pos) <= 20) {
        threats.push(shell.targetPos);
    }

    // avoid the splash of boulders
    var boulder = findNearestTargetPosTo(unit.pos, boulders);
    if (boulder && boulder.targetPos.distance(unit.pos) <= 15) {
        threats.push(boulder.targetPos);
    }

    // avoid soldiers
    var soldier = findNearestTo(unit.pos, enemySoldiers);
    if (soldier && soldier.pos.distance(unit.pos) <= 10) {
        threats.push(soldier.pos);
    }

    // avoid the goliath
    if (unit.pos.distance(goliath.pos) <= 18) {
        threats.push(goliath.pos);
    }

    // if we have threats,
    // flee in a direction leading away from them
    if (threats.length > 0) {
        if (unit.pos.y > 90) {
            threats.push(new Vector(unit.pos.x, 95));
        }
        else if (unit.pos.y < 5) {
            threats.push(new Vector(unit.pos.x, 0));
        }
        else if (unit.pos.x < 5) {
            threats.push(new Vector(0, unit.pos.y));
        }
        else if (unit.pos.x > 110) {
            threats.push(new Vector(115, unit.pos.y));
        }

        var fleeDirection = new Vector(0, 0);
        for (let threat of threats) {
            var localFleeDirection = Vector.normalize(
                    Vector.subtract(unit.pos, threat));

            // if we got no direction,
            // use the direction of home base
            if (localFleeDirection.magnitude() < 0.8) {
                localFleeDirection = Vector.normalize(
                        Vector.subtract(pointsMap.nearCorner.pos, unit.pos));
            }
            fleeDirection = Vector.add(fleeDirection, localFleeDirection);
        }

        fleeDirection = Vector.normalize(fleeDirection);
        if (fleeDirection.magnitude() < 0.8) {
            fleeDirection = Vector.normalize(
                    Vector.subtract(pointsMap.nearCorner.pos, unit.pos));
        }

        var fleePos = Vector.add(unit.pos, Vector.multiply(fleeDirection, 20));
        this.command(unit, "move", fleePos);
        return;
    }

    // find the lowest health target and shoot it
    var enemiesInRange;
    if (this.now() < 15) {
        enemiesInRange = findInRadiusOfUnit(unit, ARCHER_RANGE, removeType(GOLIATH_TYPE, enemies));
    }
    else {
        enemiesInRange = findInRadiusOfUnit(unit, ARCHER_RANGE, enemies);
    }
    var enemy = findLowestHealthNearest(unit, enemiesInRange);
    if (enemy) {
        this.command(unit, "attack", enemy);
        return;
    }

    if (defendPoint) {
        var pointDistance = unit.pos.distance(defendPoint.pos);
        if (defendPoint.team !== this.team || pointDistance >= 9) {
            this.command(unit, "move", defendPoint.pos);
            return;
        }
        else {
            this.command(unit, "move", unit.pos);
            return;
        }
    }

    // seek out and destroy the nearest archer, soldier or artillery
    var nearestEnemy = findNearestTo(unit.pos, removeType(GOLIATH_TYPE, removeType(TOWER_TYPE, enemies)));
    if (nearestEnemy) {
        this.command(unit, "attack", nearestEnemy);
        return;
    }

    // attack whatever is left
    this.command(unit, "attack", findNearestTo(unit.pos, enemies));
};

this.commandArmy = function() {
    this.allocateAndCommandBasic();
    var artillery = this.findByType(ARTILLERY_TYPE, friends);
    for (let a of artillery) {
        this.commandArtillery(a);
    }
    var towers = this.findByType(TOWER_TYPE, friends);
    for (let t of towers) {
        this.commandTower(t);
    }

    // decide the goliath defend point.
    // Thanks, Nick63 Cheesy strat.
    var nearADistance = goliath.pos.distance(pointsMap.nearA.pos);
    var nearBDistance = goliath.pos.distance(pointsMap.nearB.pos);
    var nearCornerDistance = goliath.pos.distance(pointsMap.nearCorner.pos);
    if (nearADistance < 25) {
        goliathDefendPos = pointsMap.nearA.pos;
    }
    else if (nearBDistance < 25) {
        goliathDefendPos = pointsMap.nearB.pos;
    }
    else if (nearCornerDistance < 25) {
        goliathDefendPos = pointsMap.nearCorner.pos;
    }
    else {
        goliathDefendPos = pointsMap.center.pos;
    }
};

// hero control ----------------------------------------------------------------

var throwArcherTime = -Infinity;

this.controlHero = function(defendPos) {
    // look for towers near nearA and nearB points
    // and get rid of them.
    // Nice strategy, solarflare.
    var nearATower = firstInRadiusOfPosition(pointsMap.nearA.pos, 15, enemyTowers);
    if (nearATower) {
        this.attack(nearATower);
        return;
    }
    var nearBTower = firstInRadiusOfPosition(pointsMap.nearB.pos, 15, enemyTowers);
    if (nearBTower) {
        this.attack(nearBTower);
        return;
    }

    // stomp if there are multiple units in range
    if (this.isReady("stomp")) {
        var enemiesInStompRange = this.findInRadius(15, enemies);
        if (enemiesInStompRange.length >= 3) {
            this.stomp();
            return;
        }
    }

    var nearestTower = this.findNearest(enemyTowers);

    // pick a target to throw at
    if (this.isReady("throw")) {
        // throw a boulder to hit artillery in range
        var nearestArtillery = this.findNearest(enemyArtillery);
        if (nearestArtillery && this.distanceTo(nearestArtillery) <= 25) {
            this.throw(nearestArtillery);
            return;
        }

        // throw a boulder to hit towers in range
        if (nearestTower && this.distanceTo(nearestTower) <= 25) {
            this.throw(nearestTower);
            return;
        }

        // throw a boulder to hit archers in range
        var nearestArcher = this.findNearest(enemyArchers);
        if (nearestArcher && this.distanceTo(nearestArcher) <= 25) {
            this.throw(nearestArcher);
            throwArcherTime = this.now();
            return;
        }
    }

    // try to throw the enemy goliath out of range of the point
    if (this.isReady("hurl") && this.distanceTo(goliath) <= 6
            && this.pos.distance(pointsMap.farCorner.pos) < goliath.pos.distance(pointsMap.farCorner.pos)) {
        this.hurl(goliath, pointsMap.farCorner.pos);
        return;
    }
    if (this.isReady("stomp") && this.distanceTo(goliath) <= 10) {
        this.stomp();
        return;
    }

    // attack any nearby arrow towers
    if (nearestTower && this.distanceTo(nearestTower) < 15) {
        this.attack(nearestTower);
        return;
    }

    // attack any nearby soldiers and artillery
    var slowEnemies = removeType(ARCHER_TYPE, removeType(GOLIATH_TYPE, enemies));
    if (slowEnemies.length > 0) {
        var nearestEnemy = findNearestTo(defendPos, slowEnemies);
        if (defendPos.distance(nearestEnemy.pos) < 15) {
            this.attack(nearestEnemy);
            return;
        }
    }

    // advance towards the objective
    if (pointsMap.center.team !== this.team
            && this.pos.distance(defendPos) > 4) {
        this.move(defendPos);
        return;
    }

    // attack the enemy goliath if they are threatening the objective
    if (defendPos.distance(goliath.pos) < 15) {

        // sometimes we get stuck with a friendly tower between us
        // and the enemy goliath.
        // we need to detect this and go around the tower.
        var nearestFriendlyTower = this.findNearest(friendlyTowers);
        if (nearestFriendlyTower) {
            var towerVec = Vector.subtract(nearestFriendlyTower.pos, this.pos);
            var goliathVec = Vector.subtract(goliath.pos, this.pos);
            var towerDist = towerVec.magnitude();
            var goliathDist = goliathVec.magnitude();
            if (towerDist <= 6 && towerDist < goliathDist) {
                var towerAngle = towerVec.heading();
                var goliathAngle = goliathVec.heading();
                if (Math.abs(towerAngle - goliathAngle) < Math.PI/4) {
                    this.move(Vector.add(this.pos, Vector.rotate(goliathVec, -Math.PI/2)));
                    return;
                }
            }
        }

        this.attack(goliath);
        return;
    }

    this.move(defendPos);
};

// globals

var enemies;
var enemyArchers;
var enemySoldiers;
var enemyTowers;
var enemyArtillery;
var friends;
var friendlyTowers;
var goliath;
var missiles;
var shells;
var boulders;
var pointsMap;

var goliathDefendPos;

// main loop -------------------------------------------------------------------

this.updateGlobals = function() {
    enemies = removeType(YAK_TYPE, this.findEnemies());
    enemySoldiers = this.findByType(SOLDIER_TYPE, enemies);
    enemyArchers = this.findByType(ARCHER_TYPE, enemies);
    enemyTowers = this.findByType(TOWER_TYPE, enemies);
    enemyArtillery = this.findByType(ARTILLERY_TYPE, enemies);
    friends = this.findFriends();
    friendlyTowers = this.findByType(TOWER_TYPE, friends);
    goliath = firstOfType(GOLIATH_TYPE, enemies);
    missiles = this.findEnemyMissiles();
    shells = this.findByType(SHELL_TYPE, missiles);
    boulders = this.findByType(BOULDER_TYPE, missiles);
    pointsMap = this.getControlPointsMap();

    if (!goliath) {
        // There's some broken player floating around who spawns tharin,
        // the knight, instead of their goliath.
        goliath = firstOfType("knight", enemies);
    }
};

// opening moves
var buildOffsetX, buildOffsetY;
if (this.team === "humans") {
    buildOffsetX = 4.2;
    buildOffsetY = 4.2;
}
else {
    buildOffsetX = -4.2;
    buildOffsetY = -4.2;
}

var initialCount = 0;


// center archers
this.buildXY(ARCHER_TYPE, this.pos.x + buildOffsetX, this.pos.y + buildOffsetY);
this.command(this.findFriends()[++initialCount], "move", this.getControlPointsMap().center.pos);

this.buildXY(ARCHER_TYPE, this.pos.x + buildOffsetX, this.pos.y + buildOffsetY);
this.command(this.findFriends()[++initialCount], "move", this.getControlPointsMap().center.pos);

this.buildXY(ARCHER_TYPE, this.pos.x + buildOffsetX, this.pos.y + buildOffsetY);
this.command(this.findFriends()[++initialCount], "move", this.getControlPointsMap().center.pos);

// side archers
this.buildXY(ARCHER_TYPE, this.pos.x + buildOffsetX, this.pos.y - buildOffsetY);
this.command(this.findFriends()[++initialCount], "move", this.getControlPointsMap().nearA.pos);

this.buildXY(ARCHER_TYPE, this.pos.x - buildOffsetX, this.pos.y + buildOffsetY);
this.command(this.findFriends()[++initialCount], "move", this.getControlPointsMap().nearB.pos);

// artillery
this.buildXY(ARTILLERY_TYPE, this.pos.x - buildOffsetX, this.pos.y + buildOffsetY);

mainloop:
for (;;) {
    this.updateGlobals();
    if (!goliath) {
        break mainloop;
    }

    this.commandArmy();
    this.updateGlobals();
    if (!goliath) {
        break mainloop;
    }

    var built = true;
    while (built) {
        built = this.buildArmy();
        this.updateGlobals();
        if (!goliath) {
            break mainloop;
        }
        this.commandArmy();
        this.updateGlobals();
        if (!goliath) {
            break mainloop;
        }
    }

    this.controlHero(goliathDefendPos);
}

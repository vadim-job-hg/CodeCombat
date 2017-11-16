function vecAdd(a, b) {
    return {
        x: a.x + b.x,
        y: a.y + b.y
    };
}
function vecSub(a, b) {
    return {
        x: a.x - b.x,
        y: a.y - b.y
    };
}
function vecMul(v, s) {
    return {
        x: v.x * s,
        y: v.y * s
    };
}
function vecLen(v) {
    return Math.sqrt(v.x * v.x + v.y * v.y);
}
function vecNorm(v) {
    var len = Math.sqrt(v.x * v.x + v.y * v.y);
    if (len === 0) {
        return {
            x: 1,
            y: 1
        };
    }
    return {
        x: v.x / len,
        y: v.y / len
    };
}
function vecDir(a, b) {
    return vecNorm({
        x: b.x - a.x,
        y: b.y - a.y
    });
}
function vecDist(a, b) {
    var x = b.x - a.x;
    var y = b.y - a.y;
    return Math.sqrt(x * x + y * y);
}
function makeBins() {
    var bins = new Array(30);
    for (var i = 0; i < 30; ++i) {
        bins[i] = [];
    }
    return bins;
}
function putInBins(items) {
    var bins = makeBins();
    for (var i = 0, len = items.length; i < len; ++i) {
        var item = items[i];
        var itemPos = item.pos;
        var binX = Math.floor(itemPos.x / 13.333333333333);
        var binY = Math.floor(itemPos.y / 14);
        if (// ignore corpses on the outskirts
            binY >= 5 || binX >= 6) {
            continue;
        }
        bins[binY * 6 + binX].push(item);
    }
    return bins;
}
function findBestBinPos(bins) {
    var winIdx;
    var winScore = -Infinity;
    for (var i = 0; i < 30; ++i) {
        var score = bins[i].length;
        if (score > winScore) {
            winScore = score;
            winIdx = i;
        }
    }
    return {
        pos: {
            x: winIdx % 6,
            y: Math.floor(winIdx / 6)
        },
        score: winScore
    };
}
function findBestBinPosAvgCoords(bins) {
    var winIdx;
    var winScore = -Infinity;
    for (var i = 0; i < 30; ++i) {
        var score = bins[i].length;
        if (score > winScore) {
            winScore = score;
            winIdx = i;
        }
    }
    var winX = 0;
    var winY = 0;
    var winBin = bins[i];
    for (var i$2 = 0, len = winBin.length; i$2 < len; ++i$2) {
        var item = winBin[i$2];
        var itemPos = item.pos;
        winX += itemPos.x;
        winY += itemPos.y;
    }
    winX /= winBin.length;
    winY /= winBin.length;
    return {
        pos: {
            x: winX,
            y: winY
        },
        score: winScore
    };
}
function findLargestGroupPosAvg(items) {
    var bins = putInBins(items);
    var data = findBestBinPos(bins);
    return data;
}
function findLargestGroupPos(items) {
    var bins = putInBins(items);
    var data = findBestBinPos(bins);
    var pos = data.pos;
    return {
        score: data.score,
        pos: {
            x: pos.x * 13.333333333333 + 6.6666666666665,
            y: pos.y * 14 + 7
        }
    };
}
function filterType(type, arr) {
    var newArr = [];
    for (var i = 0, len = arr.length; i < len; ++i) {
        var item = arr[i];
        if (item.type === type) {
            newArr.push(item);
        }
    }
    return newArr;
}
function filterNotType(type, arr) {
    var newArr = [];
    for (var i = 0, len = arr.length; i < len; ++i) {
        var item = arr[i];
        if (item.type !== type) {
            newArr.push(item);
        }
    }
    return newArr;
}
this.filterAllies = function (arr) {
    var newArr = [];
    for (var i = 0, len = arr.length; i < len; ++i) {
        var item = arr[i];
        if (item.team === this.team) {
            newArr.push(item);
        }
    }
    return newArr;
};
function firstOfType(type, arr) {
    for (var i = 0, len = arr.length; i < len; ++i) {
        var ent = arr[i];
        if (ent.type === type) {
            return ent;
        }
    }
    return null;
}
this.findInRadius = function (radius, arr) {
    var items = [];
    for (var i = 0, len = arr.length; i < len; ++i) {
        var item = arr[i];
        if (this.distanceTo(item) < radius) {
            items.push(item);
        }
    }
    return items;
};
function findInTargetRadius(target, radius, arr) {
    var items = [];
    for (var i = 0, len = arr.length; i < len; ++i) {
        var item = arr[i];
        if (target.distanceTo(item) < radius) {
            items.push(item);
        }
    }
    return items;
}
function findLowestHealth(units) {
    var winner = null;
    var winScore = Infinity;
    for (var i = 0, len = units.length; i < len; ++i) {
        var u = units[i];
        var score = u.health;
        if (score < winScore) {
            winner = u;
            winScore = score;
        }
    }
    return winner;
}
var // globals ---------------------------------------------------------------------
globals = {
    enemies: [],
    filteredEnemies: [],
    enemySoldiers: [],
    enemyArtillery: [],
    enemyArchers: [],
    enemyGriffins: [],
    enemySorc: null,
    items: [],
    corpses: [],
    friends: [],
    friendlySoldiers: [],
    friendlyArchers: [],
    friendlyGriffins: [],
    friendlyArtillery: [],
    yeti: null,
    cachedRaiseDeadTime: -Infinity,
    cachedRaiseDeadData: null,
    cachedManaBlastTime: -Infinity,
    cachedManaBlastData: null,
    lastGoldstormTime: -Infinity,
    lastSorcFearTime: -Infinity,
    lastJumpTime: -Infinity
};
this.getManaBlastData = function () {
    var time = this.now();
    if (time - globals.cachedManaBlastTime >= 0.5) {
        globals.cachedManaBlastData = findLargestGroupPosAvg(globals.filteredEnemies);
        globals.cachedManaBlastTime = time;
    }
    return globals.cachedManaBlastData;
};
this.getRaiseDeadData = function () {
    var time = this.now();
    if (time - globals.cachedRaiseDeadTime >= 2) {
        globals.cachedRaiseDeadData = findLargestGroupPos(globals.corpses);
        globals.cachedRaiseDeadTime = time;
    }
    return globals.cachedRaiseDeadData;
};
this.updateGlobals = function () {
    globals.enemies = this.findEnemies();
    globals.filteredEnemies = filterNotType('yeti', filterNotType('cage', globals.enemies));
    globals.enemySorc = firstOfType('sorcerer', globals.enemies);
    globals.enemySoldiers = filterType('soldier', globals.enemies);
    globals.enemyArchers = filterType('archer', globals.enemies);
    globals.enemyGriffins = filterType('griffin-rider', globals.enemies);
    globals.enemyArtillery = filterType('artillery', globals.enemies);
    globals.yeti = firstOfType('yeti', globals.enemies);
    globals.items = this.findItems();
    globals.corpses = this.findCorpses();
    globals.friends = this.findFriends();
    globals.friendlySoldiers = filterType('soldier', globals.friends);
    globals.friendlyArchers = filterType('archer', globals.friends);
    globals.friendlyGriffins = filterType('griffin-rider', globals.friends);
    globals.friendlyArtillery = filterType('artillery', globals.friends);
};
// Paths to the best coin via the "gravity" approach.
this.findGoalCoinPositionGravity = function (coins) {
    var forceX = 0;
    var forceY = 0;
    var pos = this.pos;
    var posX = pos.x;
    var posY = pos.y;
    var enemySorc = globals.enemySorc;
    var yeti = globals.yeti;
    var enemyIsFeared = this.now() - globals.lastSorcFearTime < 5;
    for (var i = 0, len = coins.length; i < len; ++i) {
        var coin = coins[i];
        var dist = this.distanceTo(coin);
        if (dist === 0) {
            continue;
        }
        var enemyDist = enemySorc.distanceTo(coin);
        var attractionStrength = coin.value;
        var enemyMultiplier = (dist + enemyDist) / enemyDist;
        if (enemyMultiplier > 2.22222222) {
            if (enemyIsFeared) {
                attractionStrength *= 2.22222222;
            } else {
                attractionStrength /= 2;
            }
        } else {
            attractionStrength *= enemyMultiplier;
        }
        var // Strength is attenuated based on distance squared,
        // however here we divide by distance again,
        // making it distance cubed,
        // because the direction vector is not normalized
        // and is therefore proportional to distance.
        finalStrength = attractionStrength / (dist * dist * dist);
        var coinPos = coin.pos;
        forceX += (coinPos.x - posX) * finalStrength;
        forceY += (coinPos.y - posY) * finalStrength;
    }
    if (// yeti influence
        yeti !== null) {
        var // Strength is attenuated based on distance squared,
        // however here we divide by distance again,
        // making it distance cubed,
        // because the direction vector is not normalized
        // and is therefore proportional to distance.
        yetiDist = this.distanceTo(yeti);
        if (yetiDist !== 0) {
            var yetiStrength = -20 / (yetiDist * yetiDist * yetiDist);
            var yetiPos = yeti.pos;
            forceX += (yetiPos.x - posX) * yetiStrength;
            forceY += (yetiPos.y - posY) * yetiStrength;
        }
    }
    var // wall influence
    leftWallDist = pos.x;
    var rightWallDist = 85 - pos.x;
    forceX += 1 / (leftWallDist * leftWallDist) - 1 / (rightWallDist * rightWallDist);
    var topWallDist = 72 - pos.y;
    var bottomWallDist = pos.y;
    forceY += 1 / (bottomWallDist * bottomWallDist) - 1 / (topWallDist * topWallDist);
    var finalScale = 10 / Math.sqrt(forceX * forceX + forceY * forceY);
    var newPos = {
        x: posX + forceX * finalScale,
        y: posY + forceY * finalScale
    };
    return newPos;
};
this.findGoalCoinPositionGreedy = function (coins) {
    var winner = null;
    var winScore = -Infinity;
    for (var i = 0, len = coins.length; i < len; ++i) {
        var coin = coins[i];
        var dist = this.distanceTo(coin);
        var strength = coin.value;
        if (strength === 3) {
            strength = 6;
        }
        var score = strength / dist;
        var enemyDist = globals.enemySorc.distanceTo(coin);
        if (dist > enemyDist) {
            score /= 2;
        }
        if (globals.yeti) {
            var yetiDist = globals.yeti.distanceTo(coin);
            if (dist > yetiDist) {
                score /= 4;
            }
        }
        if (score > winScore) {
            winner = coin;
            winScore = score;
        }
    }
    if (winner === null) {
        return {
            x: 40,
            y: 38
        };
    }
    return winner.pos;
};
this.findGoalCoinPositionGold = function (coins) {
    var winner = null;
    var winScore = -Infinity;
    for (var i = 0, len = coins.length; i < len; ++i) {
        var coin = coins[i];
        var strength = coin.value;
        if (strength === 3) {
            strength === 9;
        }
        var score = strength / this.distanceTo(coin);
        if (score > winScore) {
            winner = coin;
            winScore = score;
        }
    }
    return winner.pos;
};
// actions
this.collectCoinAction = function () {
    return { action: 'collect-coins' };
};
this.goldstormAction = function () {
    if (!this.canCast('goldstorm')) {
        return null;
    }
    if (this.distanceTo(globals.enemySorc) < 40) {
        return null;
    }
    return { action: 'goldstorm' };
};
this.raiseDeadAction = function () {
    if (this.now() < 5) {
        return null;
    }
    if (!this.canCast('raise-dead') && !this.isReady('reset-cooldown')) {
        return null;
    }
    var nearbyCorpses = this.findInRadius(20, globals.corpses);
    if (// do not res artillery, it does more harm than good
        firstOfType('artillery', nearbyCorpses) !== null) {
        return null;
    }
    if (// don't waste the spell for too few corpses
        nearbyCorpses.length < 2) {
        return null;
    }
    if (!this.canCast('raise-dead')) {
        return {
            action: 'reset-cooldown',
            target: 'raise-dead'
        };
    } else {
        return { action: 'raise-dead' };
    }
};
this.attackArchersAction = function () {
    var targetArcher = findLowestHealth(this.findInRadius(25, globals.enemyArchers));
    if (targetArcher === null) {
        return null;
    }
    return {
        action: 'attack',
        target: targetArcher
    };
};
this.attackSorcInEndGameAction = function () {
    if (this.now() < 110) {
        return null;
    }
    var sorc = globals.enemySorc;
    if (sorc.health >= this.health) {
        return null;
    }
    return {
        action: 'attack',
        target: globals.enemySorc
    };
};
this.attackArtilleryAction = function () {
    if (globals.enemyArtillery.length < 1) {
        return null;
    }
    var target = this.findNearest(globals.enemyArtillery);
    if (target === null) {
        return null;
    }
    if (this.distanceTo(target) >= 40) {
        return null;
    }
    return {
        action: 'attack',
        target: target
    };
};
this.aggressiveManaBlastAction = function () {
    if (this.now() < 5) {
        return null;
    }
    if (!this.isReady('mana-blast') && !this.isReady('reset-cooldown')) {
        return null;
    }
    var manaBlastData = this.getManaBlastData();
    var enemyCount = manaBlastData.score;
    if (// don't waste the spell on too few enemies
        enemyCount <= 3) {
        return null;
    }
    var manaBlastPos = manaBlastData.pos;
    var distance = vecDist(this.pos, manaBlastPos);
    if (distance > 10) {
        return null;
    }
    if (!this.isReady('mana-blast')) {
        return {
            action: 'reset-cooldown',
            target: 'mana-blast'
        };
    } else if (distance > 3) {
        return {
            action: 'move',
            target: manaBlastPos
        };
    } else {
        return { action: 'mana-blast' };
    }
};
this.defensiveManaBlastAction = function () {
    if (!this.isReady('mana-blast') && !this.isReady('reset-cooldown')) {
        return null;
    }
    var nearEnemies = this.findInRadius(10, globals.filteredEnemies);
    if (nearEnemies.length < 5) {
        return null;
    }
    if (!this.isReady('mana-blast')) {
        return {
            action: 'reset-cooldown',
            target: 'mana-blast'
        };
    } else {
        return { action: 'mana-blast' };
    }
};
this.drainLifeAction = function () {
    if (!this.canCast('drain-life')) {
        return null;
    }
    if (this.health / this.maxHealth > 0.3) {
        return null;
    }
    var target = findLowestHealth(this.findInRadius(15, globals.enemies));
    if (target === null) {
        return null;
    }
    return {
        action: 'drain-life',
        target: target
    };
};
this.fearEnemySorcererAction = function () {
    if (this.canCast('fear')) {
        if (!this.canCast('fear', globals.enemySorc)) {
            return null;
        }
    } else if (!this.isReady('reset-cooldown')) {
        return null;
    }
    if (this.distanceTo(globals.enemySorc) > 25 + 10) {
        return null;
    }
    if (!this.canCast('fear')) {
        return {
            action: 'reset-cooldown',
            target: 'fear'
        };
    } else {
        return {
            action: 'fear',
            target: globals.enemySorc
        };
    }
};
this.fearYetiAction = function () {
    if (globals.yeti === null) {
        return null;
    }
    if (this.canCast('fear')) {
        if (!this.canCast('fear', globals.yeti)) {
            return null;
        }
    } else if (!this.isReady('reset-cooldown')) {
        return null;
    }
    if (this.distanceTo(globals.yeti) > 20) {
        return null;
    }
    if (globals.yeti.target !== this) {
        return null;
    }
    if (!this.canCast('fear')) {
        return {
            action: 'reset-cooldown',
            target: 'fear'
        };
    } else {
        return {
            action: 'fear',
            target: globals.yeti
        };
    }
};
this.avoidYetiAction = function () {
    if (!globals.yeti) {
        return null;
    }
    if (this.distanceTo(globals.yeti) > 20) {
        return null;
    }
    // the coin collection algorithm devalues coins near the yeti
    // so it should steer us away.
    return { action: 'collect-coins' };
};
// action selection and execution logic
this.goToTarget = function (pos) {
    pos = this.pathAroundBox(pos);
    if (this.isReady('jump') && vecDist(this.pos, pos) >= 8) {
        this.jumpTo(pos);
        globals.lastJumpTime = this.now();
    } else {
        this.move(pos);
    }
};
this.pathAroundBox = function (pos) {
    var box = firstOfType('cage', globals.enemies);
    if (box === null) {
        return pos;
    }
    if (this.distanceTo(box) > 7) {
        return pos;
    }
    if (this.pos.y < box.pos.y && pos.y > box.pos.y || this.pos.y > box.pos.y && pos.y < box.pos.y) {
        if (// our path crosses the box's y position
            this.pos.x <= box.pos.x + 4 && this.pos.x >= box.pos.x - 4) {
            if (// we are overlapping the box on the x axis
                pos.x > box.pos.x) {
                return {
                    // target is on the right, move right
                    x: pos.x + 10,
                    y: pos.y
                };
            } else {
                return {
                    // target is on the left, move left
                    x: pos.x - 10,
                    y: pos.y
                };
            }
        }
    }
    if (this.pos.x < box.pos.x && pos.x > box.pos.x || this.pos.x > box.pos.x && pos.y < box.pos.x) {
        if (// our path crosses the box's x position
            this.pos.y <= box.pos.y + 4 && this.pos.y >= box.pos.y - 4) {
            if (// we are overlapping the box on the y axis
                pos.y > box.pos.y) {
                return {
                    // target is above, move up
                    x: pos.x,
                    y: pos.y + 10
                };
            } else {
                return {
                    // target is below, move down
                    x: pos.x,
                    y: pos.y - 10
                };
            }
        }
    }
    return pos;
};
this.executeAction = function (action$2) {
    switch (action$2.action) {
    case 'move':
        this.goToTarget(action$2.target);
        return;
    case 'collect-coins':
        var coinPos;
        var timeSinceGS = this.now() - globals.lastGoldstormTime;
        if (timeSinceGS > 0.5 && timeSinceGS < 10) {
            coinPos = this.findGoalCoinPositionGold(globals.items);
        } else {
            coinPos = this.findGoalCoinPositionGravity(globals.items);
        }
        this.goToTarget(coinPos);
        return;
    case 'attack':
        this.attack(action$2.target);
        return;
    case 'raise-dead':
        this.cast('raise-dead');
        return;
    case 'mana-blast':
        this.manaBlast();
        return;
    case 'drain-life':
        this.cast('drain-life', action$2.target);
        return;
    case 'fear':
        this.cast('fear', action$2.target);
        if (action$2.target === globals.enemySorc) {
            globals.lastSorcFearTime = this.now();
        }
        return;
    case 'goldstorm':
        this.cast('goldstorm');
        globals.lastGoldstormTime = this.now();
        return;
    case 'reset-cooldown':
        this.resetCooldown(action$2.target);
        return;
    default:
        this.debug('How do I ' + action$2.type + '?');
        return;
    }
};
this.selectAction = function () {
    var action$2;
    action$2 = //this.fearYetiAction,
    //this.drainLifeAction,
    //this.fearEnemySorcererAction,
    this.avoidYetiAction();
    if (action$2 !== null) {
        return action$2;
    }
    action$2 = this.raiseDeadAction();
    if (action$2 !== null) {
        return action$2;
    }
    action$2 = this.aggressiveManaBlastAction();
    if (action$2 !== null) {
        return action$2;
    }
    action$2 = this.defensiveManaBlastAction();
    if (action$2 !== null) {
        return action$2;
    }
    action$2 = //this.attackArchersAction,
    this.attackArtilleryAction();
    if (action$2 !== null) {
        return action$2;
    }
    action$2 = this.attackSorcInEndGameAction();
    if (action$2 !== null) {
        return action$2;
    }
    action$2 = this.goldstormAction();
    if (action$2 !== null) {
        return action$2;
    }
    action$2 = this.collectCoinAction();
    if (action$2 !== null) {
        return action$2;
    }
};
// ability use and movement ----------------------------------------------------
this.doAbilityLogic = function () {
    this.executeAction(this.selectAction());
};
// army summoning --------------------------------------------------------------
this.percentageSummon = function () {
    var griffinCount = globals.friendlyGriffins.length;
    var soldierCount = globals.friendlySoldiers.length;
    if (griffinCount < 3) {
        return 'griffin-rider';
    }
    if (soldierCount < 5) {
        return 'soldier';
    }
    if (soldierCount / griffinCount < 0.666666) {
        return 'soldier';
    }
    return 'griffin-rider';
};
this.decideSummon = function () {
    var //if (this.now() > 30)  {
    //    return "griffin-rider";
    //}
    nearestEnemy = this.findNearest(globals.filteredEnemies);
    if (// spawn troops if the enemy is near.
        // if it's the early game, don't spawn unless they have military
        // (i.e. more than just the sorc)
        this.distanceTo(nearestEnemy) < 30 && (this.now() > 45 || globals.filteredEnemies.length > 1)) {
        return this.percentageSummon();
    }
    if (this.shouldDoEndGameAttack()) {
        return this.percentageSummon();
    }
    if (this.shouldGoOffensive()) {
        return this.percentageSummon();
    }
    if (this.gold >= 150) {
        return 'griffin-rider';
    }
    return null;
};
this.shouldDoEndGameAttack = function () {
    return this.now() > 105 && globals.friends.length > globals.filteredEnemies.length;
};
this.shouldGoOffensive = function () {
    return globals.friends.length > 9 && globals.friends.length / globals.filteredEnemies.length > 2;
};
this.doSummonLogic = function () {
    var summonType = this.decideSummon();
    var // if we summon while jumping we seem to always crash due to
    // "cannot read property z of null"
    timeSinceJump = this.now() - globals.lastJumpTime;
    if (timeSinceJump > 0.5) {
        while (summonType !== null && this.gold > this.costOf(summonType)) {
            this.summon(summonType);
            this.updateGlobals();
            summonType = this.decideSummon();
        }
        return true;
    }
    return false;
};
this.doAttackNearestAI = function (enemies, units) {
    for (var i = 0, len = units.length; i < len; ++i) {
        var unit = units[i];
        var nearestEnemy = unit.findNearest(enemies);
        this.command(unit, 'attack', nearestEnemy);
    }
};
this.selectRoamTarget = function (unit) {
    var target = unit.findNearest(globals.enemyArtillery);
    if (target !== null) {
        return target;
    }
    target = unit.findNearest(globals.enemyArchers);
    if (target !== null) {
        return target;
    }
    target = unit.findNearest(globals.enemyGriffins);
    if (target !== null) {
        return target;
    }
    //target = unit.findNearest(globals.enemySoldiers);
    //if (target !== null) {
    //    return target;
    //}
    return globals.enemySorc;
};
this.pickRandomPosition = function () {
    return {
        x: Math.random() * 83,
        y: Math.random() * 70
    };
};
this.maybeKiteSoldiers = function (leader, units) {
    var leaderPos = leader.pos;
    var nearestSoldier = leader.findNearest(globals.enemySoldiers);
    if (nearestSoldier !== null) {
        var soldierDistance = leader.distanceTo(nearestSoldier);
        if (soldierDistance < 10) {
            var soldierPos = nearestSoldier.pos;
            var offsetScale = soldierDistance === 0 ? 10 : 10 / soldierDistance;
            var newPos = {
                x: leaderPos.x + (leaderPos.x - soldierPos.x) * offsetScale,
                y: leaderPos.y + (leaderPos.y - soldierPos.y) * offsetScale
            };
            var len = units.length;
            for (var i = 0; i < len; ++i) {
                this.command(units[i], 'move', newPos);
            }
            return true;
        }
    }
    return false;
};
this.doRoamAttackAI = function (units) {
    if (units.length === 0) {
        return;
    }
    var leader = units[0];
    if (this.maybeKiteSoldiers(leader, units)) {
        return;
    }
    var target = this.selectRoamTarget(leader);
    var len = units.length;
    for (var i = 0; i < len; ++i) {
        this.command(units[i], 'attack', target);
    }
};
this.doAttackTargetAndKiteAI = function (target, units) {
    if (units.length === 0) {
        return;
    }
    var leader = units[0];
    if (this.maybeKiteSoldiers(leader, units)) {
        return;
    }
    var len = units.length;
    for (var i = 0; i < len; ++i) {
        this.command(units[i], 'attack', target);
    }
};
this.doAttackTargetAI = function (target, units) {
    if (units.length === 0) {
        return;
    }
    var len = units.length;
    for (var i = 0; i < len; ++i) {
        this.command(units[i], 'attack', target);
    }
};
this.doAttackSpecificAI = function (units) {
    if (units.length === 0) {
        return;
    }
    var target = units[0].findNearest(globals.filteredEnemies);
    var len = units.length;
    for (var i = 0; i < len; ++i) {
        this.command(units[i], 'attack', target);
    }
};
this.maybeKiteIndividual = function (unit, enemies) {
    var nearestSoldier = unit.findNearest(enemies);
    if (nearestSoldier !== null) {
        var soldierDistance = unit.distanceTo(nearestSoldier);
        if (soldierDistance < 6) {
            var soldierPos = nearestSoldier.pos;
            var offsetScale = soldierDistance === 0 ? 10 : 10 / soldierDistance;
            var unitPos = unit.pos;
            var newPos = {
                x: unitPos.x + (unitPos.x - soldierPos.x) * offsetScale,
                y: unitPos.y + (unitPos.y - soldierPos.y) * offsetScale
            };
            this.command(unit, 'move', newPos);
            return true;
        }
    }
    return false;
};
this.doDefensiveGriffinAI = function (units) {
    var enemySoldiers = globals.enemySoldiers;
    var heroPos = this.pos;
    var offsetHeroPos = {
        x: heroPos.x + 2,
        y: heroPos.y + 2
    };
    var yeti = globals.yeti;
    var yetiArr = [yeti];
    var artillery = globals.enemyArtillery.length > 0 ? globals.enemyArtillery[0] : null;
    if (artillery !== null && enemySoldiers.length === 0) {
        var len = units.length;
        for (var i = 0; i < len; ++i) {
            this.command(units[i], 'attack', artillery);
        }
        return;
    }
    for (var i$2 = 0, len$2 = units.length; i$2 < len$2; ++i$2) {
        var unit = units[i$2];
        if (this.maybeKiteIndividual(unit, enemySoldiers)) {
            continue;
        }
        if (yeti !== null && this.maybeKiteIndividual(unit, yetiArr)) {
            continue;
        }
        var lowestHealthEnemy = findLowestHealth(findInTargetRadius(unit, 20, globals.filteredEnemies));
        if (lowestHealthEnemy !== null) {
            this.command(unit, 'attack', lowestHealthEnemy);
            continue;
        }
        this.command(unit, 'move', offsetHeroPos);
    }
};
this.doOffensiveGriffinAI = function (units) {
    var enemySoldiers = globals.enemySoldiers;
    var enemyRanged = globals.enemyGriffins.concat(globals.enemyArchers, globals.enemyArtillery);
    var sorc = globals.enemySorc;
    var yeti = globals.yeti;
    var yetiArr = [yeti];
    for (var i = 0, len = units.length; i < len; ++i) {
        var unit = units[i];
        if (this.maybeKiteIndividual(unit, enemySoldiers)) {
            continue;
        }
        if (yeti !== null && this.maybeKiteIndividual(unit, yetiArr)) {
            continue;
        }
        var // prioritize ranged units, they are a threat to us
        lowestHealthRanged = findLowestHealth(findInTargetRadius(unit, 20, enemyRanged));
        if (lowestHealthRanged !== null) {
            this.command(unit, 'attack', lowestHealthRanged);
            continue;
        }
        if (// kill the sorc if in range
            unit.distanceTo(sorc) < 20) {
            this.command(unit, 'attack', sorc);
            continue;
        }
        var // otherwise clean up soldiers
        lowestHealthSoldier = findLowestHealth(findInTargetRadius(unit, 20, enemySoldiers));
        if (lowestHealthSoldier !== null) {
            this.command(unit, 'attack', lowestHealthSoldier);
            continue;
        }
        var nearestEnemy = this.findNearest(globals.filteredEnemies);
        this.command(unit, 'attack', nearestEnemy);
    }
};
this.doDefensiveTroopLogic = function () {
    this.doAttackNearestAI(globals.filteredEnemies, globals.friendlySoldiers);
    this.doDefensiveGriffinAI(globals.friendlyGriffins);
};
this.doOffensiveTroopLogic = function () {
    this.doAttackNearestAI(globals.enemies, globals.friendlySoldiers);
    this.doOffensiveGriffinAI(globals.friendlyGriffins);
};
this.doEndGameTroopLogic = function () {
    this.doAttackTargetAI(globals.enemySorc, globals.friends);
};
this.doTroopLogic = function () {
    if (//var grifCount = globals.friendlyGriffins.length;
        //var enemyGrifCount = globals.enemyGriffins.length;
        //if (grifCount > 4 && grifCount / enemyGrifCount >= 1.8) {
        //    this.doOffensiveTroopLogic();
        //}
        //else {
        //    this.doDefensiveTroopLogic();
        //}
        this.shouldDoEndGameAttack()) {
        this.doEndGameTroopLogic();
    } else if (this.shouldGoOffensive()) {
        this.doOffensiveTroopLogic();
    } else {
        this.doDefensiveTroopLogic();
    }
};
if (// main loop -------------------------------------------------------------------
    // There's some broken player floating around who spawns tharin,
    // the knight, instead of their sorc.
    // Just kill this guy.
    this.findEnemies()[0].type === 'knight') {
    loop {
        this.attack(this.findEnemies()[0]);
    }
}
for (;;) {
    this.updateGlobals();
    if (globals.enemySorc === null) {
        return;
    }
    // command troops
    this.doTroopLogic();
    // "emergency" actions that take priority over summoning
    var action;
    action = this.fearYetiAction();
    if (action !== null) {
        this.executeAction(action);
        continue;
    }
    action = this.fearEnemySorcererAction();
    if (action !== null) {
        this.executeAction(action);
        continue;
    }
    // summon troops
    this.doSummonLogic();
    // use abilities and collect coins
    this.doAbilityLogic();
}
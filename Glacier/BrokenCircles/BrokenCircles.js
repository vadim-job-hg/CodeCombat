Can you get a Python version of this?
 * Created by knubisoft-1 on 11.08.2016.
 */
var r = 10;
var diff = 0.5;
var threshold = 5.7;
var S = 3;
var circle = 5;
var cx = 68,
    cy = 68;

// hero.moveXY(132, 70);
// hero.stomp();

function prepareMap() {
    var map = [];
    for (var y = 0; y < 135; y++) {
        var row = [];
        for (var x = 0; x < 160; x++) {
            row.push(0);
        }
        map.push(row);
    }
    var hazards = hero.findHazards();
    for (var i = 0; i < hazards.length; i++) {
        var hx = Math.round(hazards[i].pos.x);
        var hy = Math.round(hazards[i].pos.y);
        map[hx][hy] = 1;
    }
    return map;
}

function buildRect(x1, y1, x2, y2) {
    if (x1 === x2) {
        return [[x1 - S, y1], [x1 + S, y1], [x2 - S, y2], [x2 + S, y2]];
    }
    var tang = (y1 - y2) / (x1 - x2);
    var ang = Math.atan(tang);
}

var rad = Math.PI * 2 / 360;

hero.moveXY(128 - r / 2 - diff, 68);

// var iceM = prepareMap();
var angle = 0;
while(true) {
    if (!circle) {
        break;
    }
    var R = r * circle + r / 2 - diff;
    var iR = R - r;
    while (true) {
        angle = (angle + 2) % 360;
        var x = cx + Math.cos(angle * rad) * R;
        var y = cy + Math.sin(angle * rad) * R;
        var ix = cx + Math.cos(angle * rad) * iR;
        var iy = cy + Math.sin(angle * rad) * iR;
        // buildRect(x, y, ix, iy);
        // hero.debug(hero.isPathClear({x: x, y: y}, {x: ix, y: iy}));
        // hero.say(x);
        // hero.say(y);
        hero.moveXY(x, y);
        var nearest = hero.findNearest(hero.findHazards());

        if (hero.distanceTo(nearest) >= threshold) {
            hero.debug(angle, hero.distanceTo(nearest));
            // hero.say(nearest.pos.x + "-" + nearest.pos.y);
            // hero.say(ix + "-" + iy);
            hero.moveXY(ix, iy);
            // hero.say(nearest.pos.x + "-" + nearest.pos.y);
            circle--;
            break;
        }
    }
}

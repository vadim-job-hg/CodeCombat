//http://codecombat.com/play/level/ogres-of-hanoi
var that = this;

function hanoi(n, from, to, via) {
    if (n === 1) {
        that.say("move", [from, to]);
    } else {
        hanoi(n - 1, from, via, to);
        that.say("move", [from, to]);
        hanoi(n - 1, via, to, from);
    }
}

hanoi(5, 2, 3, 1);

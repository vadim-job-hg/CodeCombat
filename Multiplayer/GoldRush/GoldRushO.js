//http://codecombat.com/play/ladder/gold-rush
this.closest = function (items) {
    var coor;
    var cost = 0;
    var dist = 9999;
    var jumpok = 0;
    var bonus = 0;
    for (var i = 0; i < items.length; i++) {
        bonus = 0;
        if (items[i].bountyGold == 5) bonus = 20;
        if (items[i].bountyGold == 4) bonus = 10;
        if (this.distance(items[i]) - (items[i].bountyGold - cost) * 10 < dist + bonus) {
            cost = items[i].bountyGold;
            coor = items[i].pos;
            dist = this.distance(items[i]) - bonus - (items[i].bountyGold - cost) * 10;
        }
    }
    var jump = this.getCooldown("jump");
    if (cost != 5) {
        for (i = 0; i < items.length; i++) {
            if (((this.distance(items[i]) < 10 && cost < 5) || (this.distance(items[i]) < 5 && cost == 5)) && this.distance(items[i]) < dist) {
                cost = items[i].bountyGold;
                coor = items[i].pos;
                dist = this.distance(items[i]);
            }
        }

    }
    if (((dist > 10 && dist < 30) || cost == 5) && jump == "0") {
        jumpok = 1;
    }
    if (jumpok == 1 && typeof(coor) != "undefined") {
        this.jumpTo(coor);
    }
    else {
        if (typeof(coor) != "undefined") this.move(coor);
    }
};
this.closest(this.getItems());






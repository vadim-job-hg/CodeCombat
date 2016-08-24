//https://codecombat.com/play/level/javascript-a-fine-mint
// Батраки пытаются украсть Ваши монеты!
// Напишите функцию, чтобы раздавить их, прежде чем они смогут взять Ваши монеты.

function pickUpCoin() {
    var coin = hero.findNearestItem();
    if(coin) {
        hero.moveXY(coin.pos.x, coin.pos.y);
    }
}

// Напишите функцию attackEnemy ниже.
// Найдите ближайшего противника и атакуйте их, если они существуют!
function attackEnemy(){
    var enemy = hero.findNearestEnemy();
    if(enemy){
        hero.say(enemy);
        hero.attack(enemy);
    }
}

while(true) {
    attackEnemy(); // ∆ Раскомментируйте эту строку после того, как Вы напишете функцию attackEnemy.
    pickUpCoin();
}

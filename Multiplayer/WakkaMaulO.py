// Добро пожаловать в Wakka Maul! Приготовтесь к битве!
// Отважтесь пройти этот лабиринт и соберите свои сокровища.
// Разламывайте двери чтобы освободить союзников (или врагов).
// Например, чтобы атаковать дверь с отметкой "g" используйте:
//this.attack("d");
// Если у вас достаточно золота, вы можете позвать на помощь называя определённый тип юнита чтобы призвать его!
//this.say("thrower"); чтобы призвать двух Метателей (Thrower) по 9 золотых за каждого!
//this.say("scout"); чтобы призвать Скаута (Scout) за 18 золотых!

this.moveUp();
this.moveLeft();
this.attack("d");
this.say("scout");
this.moveLeft();
this.moveDown();
this.moveDown();
this.moveLeft();
this.moveUp();
this.moveUp();
this.moveLeft();
this.moveLeft();
this.moveDown();
this.attack("c");
this.attack("b");
this.say("thrower");
this.say("scout");
this.say("scout");
this.say("scout");
this.say("scout");
this.say("scout");
this.say("scout");
this.say("scout");
this.say("scout");
this.say("scout");
this.say("scout");
this.say("scout");
this.say("scout");
this.moveDown();
this.moveDown();
this.moveDown();
this.moveDown();
this.say("scout");
this.say("scout");
this.say("scout");
this.say("scout");
this.say("scout");
this.say("scout");
this.say("scout");
this.say("scout");
this.say("scout");
this.say("scout");
enemy = this.findNearestEnemy();
while (enemy && enemy.health > 0) {
    this.attack(enemy);
}

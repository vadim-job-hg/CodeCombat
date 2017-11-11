//https://codecombat.com/play/level/forest-incursion
// Okar needs to stomp out these annoying little munchkins!
// Unfortunately he is slow, and his attacks do little damage.
// Fortunately, as a game developer, you have full control over the world!
// Set Okar's properties to buff him up for ogre slaying!

game.addDefeatGoal();
game.addSurviveGoal();
var hero = game.spawnHeroXY(12, 10);
// Increase the hero's maxSpeed, so he runs faster.
hero.maxSpeed = 25;
// Increase the hero's maxHealth, so he lasts longer.
hero.maxHealth = 5000;
// Increase the hero's health, so he can actually take the hits.
hero.health = 5000;
// Increase the hero's attackDamage, so he can quickly kill the ogres.
hero.attackDamage = 5000;

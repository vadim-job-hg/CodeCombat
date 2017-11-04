// Recruit soldiers and archers to fill out each squadron.
// Each paladin has a decimal number stored in her deployment attribute.
// Convert these to binary and represent them with lines of soldiers and archers next to each paladin.
// Soldiers are 0s, archers are 1s.
// For the bonus goal, add griffins as 2s for trinary number lines next to the warlocks.
// Check the guide for help with binary numbers.

function toBinary(number)
    {
    var string = "";
    while(string.length<8)
        {
        var remainder = number % 2;
        number = (number - remainder) / 2;
        string = remainder + string;
        }
    return string;
    }

function toTernary(number)
    {
    var string = "";
    while(string.length<8)
        {
        var remainder = number % 3;
        number = (number - remainder) / 3;
        string = remainder + string;
        }
    return string;
    }

var paladins = hero.findByType("paladin");
for(var pi=0;pi<paladins.length;pi++)
    {
    var paladin = paladins[pi];
    var number = toBinary(paladin.deployment);
    for(var ni=0;ni<number.length;ni++)
        {
        var character = number[ni];
        if (character == 1)
            {
            hero.summon("archer");
            }
        else
            {
            hero.summon("soldier");
            }
        }
    }

var warlocks = hero.findByType("warlock");
for(var wi=0;wi<warlocks.length;wi++)
    {
    var warlock = warlocks[wi];
    var number = toTernary(warlock.deployment);
    for(var ni=0;ni<number.length;ni++)
        {
        var character = number[ni];
        if (character == 1)
            {
            hero.summon("archer");
            }
        else if (character == 2)
            {
            hero.summon("griffin-rider");
            }
        else
            {
            hero.summon("soldier");
            }
        }
    }

var friends = hero.built;
var newX = 20;
var newY = 56;
for(var fi=0;fi<friends.length;fi++)
    {
    var friend = friends[fi];
    if (newX<60)
        {
        hero.command(friend, "move", {x: newX, y: newY});
        newX = newX + 5;
        }
    else if (newY>29)
        {
        newX = 20;
        newY = newY - 7;
        hero.command(friend, "move", {x: newX, y: newY});
        newX = newX + 5;
        }
    else
        {
        newX = 20;
        newY = newY - 10;
        hero.command(friend, "move", {x: newX, y: newY});
        newX = newX + 5;
        }
    }

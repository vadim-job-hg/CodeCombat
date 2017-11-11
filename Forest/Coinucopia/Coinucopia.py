while True:
    flag = hero.findFlag();
    if (flag):
        hero.pickUpFlag(flag)
    else:
        hero.say("Place a flag for me to go to.");

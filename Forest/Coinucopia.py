loop:
    flag = self.findFlag();
    if (flag):
        self.pickUpFlag(flag)    
    else:
        self.say("Place a flag for me to go to.");

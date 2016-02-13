# <%= survive %>
# <%= beware_outnumbered %>
# <%= need_support_of_allies. %>
loop:
    # <%= how_to_place_flags %>
    flag = self.findFlag()
    enemy = self.findNearestEnemy()
    if flag:
        self.say("I see a flag")
    elif enemy:
        self.attack(enemy)
    else:
        self.say("No enemies or flags in sight.")

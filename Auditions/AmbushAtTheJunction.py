# <%= survive %>
# <%= beware_outnumbered %>
# <%= need_support_of_allies. %>
while True:  # <%= how_to_place_flags %>
    flag = hero.findFlag()
    enemy = hero.findNearestEnemy()
    if flag:
        hero.say("I see a flag")
    elif enemy:
        hero.attack(enemy)
    else:
        hero.say("No enemies or flags in sight.")

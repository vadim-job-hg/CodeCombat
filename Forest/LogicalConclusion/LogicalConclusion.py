# http://codecombat.com/play/level/logical-conclusion
# Move to Eszter and get three secret values from her.
hero.moveXY(24, 16)
secretA = hero.findNearestFriend().getSecretA()
secretB = hero.findNearestFriend().getSecretB()
secretC = hero.findNearestFriend().getSecretC()

# Say "TRUE" to Tamas if A AND B are true, OR if C is true. Otherwise, say "FALSE."
# Remember to use parentheses to do your logic in the proper order.
tam = (secretA and secretB) or secretC
hero.moveXY(19, 26)
hero.say(tam)

# Say "TRUE" to Zsofi if A OR B is true, AND if C is true. Otherwise, say "FALSE."
Zsofi = (secretA or secretB) and secretC
hero.moveXY(26, 36)
hero.say(Zsofi)

# Say "TRUE" to Istvan if A OR C is true, AND if B OR C is true. Otherwise, say "FALSE."
Istvan = (secretA or secretC) and (secretB or secretC)
hero.moveXY(37, 34)
hero.say(Istvan)

# Say "TRUE" to Csilla if A AND B are true, OR if B is true AND C is NOT true. Otherwise, say "FALSE."
Csilla = (secretA and secretB) or (secretB and secretC)
hero.moveXY(40, 22)
hero.say(Csilla)

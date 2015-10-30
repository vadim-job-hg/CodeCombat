# Чтобы быстро собрать много золота, просто собирай золотые монеты.

loop:
    coins = self.findItems()
    coinIndex = 0    
    
    while coinIndex<len(coins):
        coin = coins[coinIndex]
        if coin.value == 3:
            self.moveXY(coin.pos.x, coin.pos.y)
        coinIndex +=1
        
        

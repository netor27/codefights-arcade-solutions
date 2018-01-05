def candles(candlesNumber, makeNew):
    '''
    When a candle finishes burning it leaves a leftover. 
    makeNew leftovers can be combined to make a new candle, which, when burning down, will in turn leave another leftover.
    You have candlesNumber candles in your possession. What's the total number of candles you can burn, 
    assuming that you create new candles as soon as you have enough leftovers?
    '''
    burned, leftovers = candlesNumber, candlesNumber
    print("burned=", burned, " leftovers=", leftovers)
    while leftovers >= makeNew:
        # create as much new candles as we can and save the new leftovers value
        newCandles = leftovers // makeNew
        leftovers = leftovers % makeNew        
        
        # burn the new candles and sum the leftovers
        burned += newCandles
        leftovers += newCandles    
    return burned


print(candles(5, 2))
print(candles(1, 2))
print(candles(3, 2))
print(candles(11, 3))
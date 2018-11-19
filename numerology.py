from random import *

items = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20,
         21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38,
         39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49]

for x in range(100):

    pickList = sample(items,6)
    print pickList
    sumOfseries = sum(pickList)
    
    
    
    numerologySum = 0
    nSum = 0
    div = sumOfseries / 10
    rem = sumOfseries % 10
    
    if rem != 0:
        numerologySum = numerologySum + rem
    if div < 10 :
        numerologySum = numerologySum + div
    else:
        while (div > 10):
            rem = div % 10
            div = div/10
            if div < 10:
                numerologySum = numerologySum + ( div + rem)
            else:
                numerologySum = numerologySum + rem
    
    if numerologySum < 10:
        nSum = numerologySum
    else:
        while (numerologySum > 0):
            rem = numerologySum % 10
            numerologySum = numerologySum/10
            if numerologySum < 10:
                nSum = nSum + ( numerologySum + rem)
                numerologySum = -1   
            else:
                nSum = numerologySum + rem
    
    if nSum == 9:
        print sumOfseries
        print nSum
        
        
        
        
        
    

    




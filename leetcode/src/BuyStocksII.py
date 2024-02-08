import sys

class Solution:
    def BuyStocksII(stocks):
        min = sys.maxsize
        profit = 0
        for i in range(0, (len(stocks)-1)):
            if(stocks[i+1] > stocks[i]):
                profit += stocks[i+1] - stocks[i]
        print(profit)


    stock = [1,2,3,4,5]
    BuyStocksII(stock)
import sys
def maxProfit():
    prices = [7,1,5,3,6,4]
    min_val = sys.maxsize
    max_profit = 0

    for i in (prices):
        if(i < min_val):
            min_val = i
        else:
            max_profit += i - min_val
            min_val = i

    print(max_profit)

maxProfit()

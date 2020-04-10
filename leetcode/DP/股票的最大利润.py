def maxProfit(prices):
    if not prices:
        return 0
    n = len(prices)
    curmin = prices[0] 
    maxprofit = 0
    for i in range(1,n):
        maxprofit = max(prices[i] - curmin, maxprofit)
        curmin = min(curmin, prices[i])
    return maxprofit

prices = [7,1,5,3,6,4]
print(maxProfit(prices))
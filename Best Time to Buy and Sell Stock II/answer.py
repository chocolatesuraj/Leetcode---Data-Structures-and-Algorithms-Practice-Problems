class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy=None
        profit=0
        for price in prices:
            if buy==None:
                buy=price
            elif(price<buy):
                buy=price
            elif(buy<price):
                profit+=price-buy
                buy=price
        return profit
                

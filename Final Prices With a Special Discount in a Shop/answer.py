class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:        
        ans=prices
        stack=[]
        for i,p in enumerate(prices):
            while stack and p<=stack[-1][0]:
                top,pos=stack.pop()
                price=top-p
                ans[pos]=price
            stack.append([p,i])
        return ans

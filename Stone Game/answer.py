class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        # or return True
        memo=[[None] * len(piles) for i in range(0,len(piles))]
        def dp(start,stop):
            
            if stop<start:
                return 0
            if memo[start][stop]!=None:
                return memo[start][stop]
            a=piles[start]-dp(start+1,stop)
            b=piles[stop]-dp(start,stop-1)
            max_profit=max(a,b)
            memo[start][stop]=max_profit
            return max_profit

        if dp(0,len(piles)-1)>0:
            return True
        return False

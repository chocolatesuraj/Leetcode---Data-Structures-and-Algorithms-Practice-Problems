class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        total=sum(stones)
        target=total//2
        memo=[[None]*total for  i in range(len(stones)+1)]
        def dp(prevsum,i):
            
            if prevsum>target:
                return total
            if memo[i][prevsum]!=None:
                return memo[i][prevsum]
            
            if i==len(stones):
                diff= total-(2*prevsum)
                memo[i][prevsum]=diff
                return diff 
            
            else:
                d1=dp(prevsum+stones[i],i+1)
                d2=dp(prevsum,i+1)
                ans=min(d1,d2)
                memo[i][prevsum]=ans
                return ans 
        
        return dp(0,0)


            
        

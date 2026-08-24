class Solution:
    def integerBreak(self, n: int) -> int:
        dp=[0]*(n+1)
        dp[1]=1
        for i in range(2,n+1):
            for j in range(0,i):
                dp[i]=max(dp[i],j*(i-j),j*dp[i-j]) # either multiple by the number itself or the maxproduct of that number . example- max product of 3 = 2*1=2 not 3 
        return dp[-1]

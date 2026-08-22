class Solution:
    def numSquares(self, n: int) -> int:
        memo=[float("inf")]*(n+1)
        memo[0]=0
        memo[1]=1
        i=1
        
        for i in range (0,n+1):
            if memo[i]!=1:
                j=1
                while(j*j<=i):
                    memo[i]=min(memo[i],1+memo[i-(j*j)])
                    j+=1
        return memo[-1]

class Solution:
    def minimumTotal(self, triangle: list[list[int]]) -> int:
        dp=[triangle[0][0]]
        for level in range(1,len(triangle)):
            newdp=[0]*(level+1)
            for i,w in enumerate(triangle[level]):
                if i==0:
                    newdp[i]=dp[i]+w
                elif i==level:
                    newdp[i]=dp[i-1]+w
                else:
                    newdp[i]=w+ min(dp[i-1],dp[i])
            dp=newdp

        # print(dp)
        return min(dp)


        

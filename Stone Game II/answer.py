class Solution:
    def stoneGameII(self, piles: List[int]) -> int:
        # memo=[[None]*len(piles) for i in range(int(math.log(len(piles),2))+2)]
        memo=[[None]*len(piles) for i in range(int(len(piles)))]

        def maxStones(pos,m):
            
            ans=-float('inf')
            curr=0
            if pos>=len(piles):
                return 0
            if memo[m-1][pos]!=None:
                return memo[m-1][pos]
            for i in range(pos,pos+(2*m)):
                
                if i>=len(piles):
                    memo[m-1][pos]=ans
                    return ans
                curr+=piles[i]
                ans=max(ans,curr-maxStones(i+1,max(m,i-pos+1) ))
            memo[m-1][pos]=ans

            return ans
        a= maxStones(0,1)
        return int((a +sum(piles))/2)





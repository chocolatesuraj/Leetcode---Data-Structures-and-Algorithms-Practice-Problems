class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        coins.sort(reverse=True)
        memo=[[-1]*(len(coins)+1) for i in range(amount+1)]
        def dp(currsum,pos):
            ans=0
            if currsum == amount:
                memo[currsum][pos]=1
                return 1
            elif currsum>amount:
                return 0
            if pos==len(coins):
                return 0
            
            if memo[currsum][pos]!=-1:
                return memo[currsum][pos]
            new =currsum +coins[pos]
            while  new <=amount:
                # print(new)
                ans+=dp(new, pos+1)
                new+=coins[pos]
            ans+=dp(currsum,pos+1)
            # print("ret",ans)
            memo[currsum][pos]=ans
            return ans

        return dp(0,0)

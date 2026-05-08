class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        memo=defaultdict(int)
        s=0
        ans=0
        memo[0]+=1
        for num in nums:
            s+=num
            if s-k in memo:
                ans+=memo[s-k]
            memo[s]+=1
        return ans

            
                
            





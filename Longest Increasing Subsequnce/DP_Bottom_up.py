class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        ans=[1]*len(nums)
        for i,num in enumerate(nums):
            curr=1
            for j in range(0,i):
                if nums[j]<num:
                    curr=max(curr,1+ans[j])
            ans[i]=curr
        return max(ans)
                         

class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        sums=[0]*k
        if int(sum(nums)/k)!=sum(nums)/k:
            return False
        target=int(sum(nums)/k)
        # print(target)
        nums.sort(reverse=True)
        def backtrack(i):
            # print(sums)
            if(i==len(nums)):
                if(sums==[int(sum(nums)/k)]*k):
                    return True
                return False
            # print(i)
            num=nums[i]
            prev=None
            for j in range(k):
                if(prev==sums[j]):
                    continue
                prev=sums[j]
                sums[j]+=num
                if(sums[j]>target):
                    sums[j]-=num
                    continue
                if backtrack(i+1):
                    return True 
                sums[j]-=num
            return False
        return backtrack(0)

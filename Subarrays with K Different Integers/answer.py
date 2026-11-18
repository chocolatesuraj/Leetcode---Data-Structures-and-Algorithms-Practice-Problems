class Solution:
    def subarraysWithKDistinct(self, nums: list[int], k: int) -> int:
        fnear,ffar,b=0,0,0
        counts=defaultdict(int)
        counts[nums[0]]=1
        ans=0

        while(b<len(nums)) :
            if len(counts)==k:
                while counts[nums[fnear]]>1:
                    counts[nums[fnear]]-=1
                    fnear+=1   
                ans+=fnear-ffar+1
                b+=1
                if b<len(nums):
                    counts[nums[b]]+=1

            elif len(counts)<k:
                b+=1
                if b<len(nums):
                    counts[nums[b]]+=1
            
            elif len(counts)>k:
                while(len(counts)>k):
                    counts[nums[fnear]]-=1
                    if counts[nums[fnear]]==0:
                        del counts[nums[fnear]]
                    fnear+=1
                ffar=fnear
        return ans 
        


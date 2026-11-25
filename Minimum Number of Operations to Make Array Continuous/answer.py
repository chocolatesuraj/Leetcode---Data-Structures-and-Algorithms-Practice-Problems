class Solution:
    def minOperations(self, nums: List[int]) -> int:
        pass
        # counts=Counter(nums)
        nums.sort()
        # print(nums)
        f=nums[0]
        b=f+len(nums)-1
        fpos=0
        bpos=0
        diff=0
        mindiff=float('inf')
        while(bpos<len(nums)):
            if bpos+1>=len(nums) or nums[bpos+1]>=b:
                if bpos+1>=len(nums) or nums[bpos+1]>b:
                    tempdiff=diff + b-nums[bpos]
                elif nums[bpos+1] == b:
                    tempdiff=diff  + nums[bpos+1]-nums[bpos]-1
                mindiff=min(tempdiff,mindiff)
                if mindiff==0:
                    return 0
                fpos+=1
                if fpos>=len(nums):
                    return mindiff
                f=nums[fpos]
                b=f+len(nums)-1
                diff-= max(0,nums[fpos] - nums[fpos-1]-1)

            elif nums[bpos+1]<b:
                prev=bpos
                bpos+=1
                while bpos+1 <len(nums) and nums[bpos+1]==nums[bpos]:
                    bpos+=1
                diff+=max(0,nums[bpos]-nums[prev]-1)
            # print(diff)


        return mindiff

            
                





        
            



        

class Solution:
    def minOperations(self, nums: List[int]) -> int:
        count=0
        splitpoint=None
        for i in range(0,len(nums)-1):
            if abs(nums[i]-nums[i+1])>1:
                splitpoint=i
                count+=1
                if count>1:
                    return -1
        if splitpoint==None and nums[0]==0:
            return 0
        elif splitpoint==None and nums[0]==len(nums)-1:
            return 1
       
        if nums[0]<=nums[splitpoint]  and nums[splitpoint+1]<=nums[len(nums)-1]: # inc inc case
            l1=splitpoint+1
            l2=len(nums)-l1
            if l1>l2:
                return min(l2+2,l1)
            if l2>=l1:
                return l1
        elif nums[0]>=nums[splitpoint]  and nums[splitpoint+1]>=nums[len(nums)-1]: # dec dec case
            l1=splitpoint+1
            l2=len(nums)-l1
            if l1>=l2:
                return l2+1
            if l2>l1:
                return l1+1
                
        return -1
                
           

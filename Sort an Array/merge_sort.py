class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:

        def mergesort(f,b):
            # print("merge")
            if f>b:
                return #[]
            if f==b:
                return #[nums[f]]
            m=(f+b)//2
            mergesort(f,m)
            mergesort(m+1,b)
            i,j=f,m+1
            ret=[]
            while (i<=m and j<=b):
                if nums[i]>nums[j]:
                    ret.append(nums[j])
                    j+=1
                else:
                    ret.append(nums[i])
                    i+=1
            ret=ret+nums[i:m+1]+nums[j:b+1]
            nums[f:b+1]=ret
            # return ret
        
        mergesort(0,len(nums)-1)
        return nums




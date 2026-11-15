class Solution:
    def findDifferentBinaryString(self, nums: list[str]) -> str:
        numset=set(nums)
        n=len(nums[0])
        ans=[0]*n
        ret=None
        def func(pos):
            if pos==n:
                nonlocal ret
                ret="".join(map(str,ans)) 
                if ret not in numset:
                    return True
                return False
            for i in range(0,2):
                ans[pos]=i
                if func(pos+1):
                    return True
        func(0)
        return ret
                                



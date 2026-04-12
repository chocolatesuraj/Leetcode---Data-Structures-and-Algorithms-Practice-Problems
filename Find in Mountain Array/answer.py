# """
# This is MountainArray's API interface.
# You should not implement it, or speculate about its implementation
# """
#class MountainArray:
#    def get(self, index: int) -> int:
#    def length(self) -> int:

class Solution:
    def findInMountainArray(self, target: int, mountainArr: 'MountainArray') -> int:
        # find split point -> peak of mountain 
        f=0
        l=mountainArr.length()
        b= l - 1
        peakval,peakpos=None,None
        while(f<=b):
            m= (f+b)//2
            # check if m is peak 
            prev = mountainArr.get(max(m-1,0))
            nex = mountainArr.get(min(m+1,l-1))
            curr=mountainArr.get(m)
            if prev<curr and curr>nex: # peak of mountain 
                peakval = curr
                peakpos=m
                break
            elif  prev<=curr and curr<=nex: # increasing side 
                f=m+1
            else:
                b=m-1
        
        def bsearchinc(f,b):
            ans=-1
            while(f<=b):
                m= (f+b)//2
                curr=mountainArr.get(m)
                if curr == target: 
                    ans=m
                    break
                elif  curr<target: 
                    f=m+1
                else:
                    b=m-1
            return ans 
        def bsearchdec(f,b):
            ans=-1
            while(f<=b):
                m= (f+b)//2
                curr=mountainArr.get(m)
                if curr == target: 
                    ans=m
                    break
                elif  curr>target: 
                    f=m+1
                else:
                    b=m-1
            return ans
        if peakval==target:
            return peakpos
        else:
            ans=bsearchinc(0,m-1)
            if ans!=-1:
                return ans 
            ans=bsearchdec(m+1,l-1)
            return ans 
        

        

            
        

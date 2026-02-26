class Solution:
    def romanToInt(self, s: str) -> int:
        
        def val(s):
            if(s=="I"):
                return 1
            if(s=="V"):
                return 5
            if(s=="X"):
                return 10
            if(s=="L"):
                return 50
            if(s=="C"):
                return 100
            if(s=="D"):
                return 500
            if(s=="M"):
                return 1000
        prev=0
        ans=0
        for letter in s[::-1]:
            n=val(letter)
            if(n>=prev):
                ans+=n
            else:
                ans-=n
            prev=n
        return ans

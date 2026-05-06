class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        spos,tpos=0,0
        while spos<len(s) and tpos<len(t):
            if s[spos]==t[tpos]:
                spos+=1
                tpos+=1
            else:
                tpos+=1
            
        if spos==len(s):
            return True
        return False

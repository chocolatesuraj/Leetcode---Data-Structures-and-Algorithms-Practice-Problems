class Solution:
    def appendCharacters(self, s: str, t: str) -> int:
        tpos,spos=0,0
        while(spos<len(s) and tpos<len(t)):
            if s[spos] == t[tpos]:
                spos+=1
                tpos+=1
            else:
                spos+=1
        return len(t)-tpos

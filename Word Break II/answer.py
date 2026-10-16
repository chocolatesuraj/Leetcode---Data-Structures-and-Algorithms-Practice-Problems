class Solution:
    def wordBreak(self, s: str, wordDict: list[str]) -> list[str]:
        wordDict=set(wordDict)
        return self.func(0,s,wordDict)

    def func(self,n,s,wordDict):
        ans=[]
        for i in range(n,len(s)+1):
            if s[n:i] in wordDict:
                word=s[n:i]
                if i==len(s):
                    return ans + [word]
                succesors = self.func(i,s,wordDict)
                for succesor in succesors:
                    ans.append(word+" "+succesor)
        return ans 
    

            

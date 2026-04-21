class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        slen=len(s)
        plen=len(p)
        memo=[[None]*(plen+1) for i in range(slen+1)]
        def dp(sptr,pptr):

            if (sptr == slen and (pptr == plen or (pptr+1==plen-1 and p[pptr+1]=="*")) ):
                memo[sptr][pptr]=True
                return True
            elif(pptr > plen or sptr>slen):
                return False
            if memo[sptr][pptr]!=None:
                return memo[sptr][pptr]
            if  pptr+1<plen and p[pptr+1]=="*":
                a,b,c=False,False,False
                if ((sptr<slen and p[pptr] == s[sptr]) or p[pptr] == "."):
                    a=dp(sptr+1,pptr)
                    c=dp(sptr+1,pptr+2)
                b=dp(sptr,pptr+2)
                

                memo[sptr][pptr] = a or b or c 
                return memo[sptr][pptr]
            elif pptr<plen and p[pptr] == ".":
                memo[sptr][pptr] =dp(sptr+1,pptr+1)
                return memo[sptr][pptr]

            elif pptr<plen and sptr<slen and s[sptr] == p[pptr]:
                memo[sptr][pptr] = dp(sptr+1,pptr+1)
                return memo[sptr][pptr]
            return False
        return dp(0,0)


class Solution:
    def totalNQueens(self, n: int) -> int:
        ans=0
        ucols,upos,uneg=set(),set(),set() # u = used / blocked
        # uneg and upos are negeative and postive diagonal - where positive is the diagonal with positive slope
        def solve(r): # r= row number 
            nonlocal ans
            row=r
            for col in range (0,n):
                if col not in ucols:
                    ucols.add(col)
                    if row-col  not in uneg and row+col not in upos:
                        uneg.add(row-col)
                        upos.add(row+col)
                        if len(ucols)==n: # and len(urows)==n and all other sets of lenght n  
                            ans+=1
                        
                        solve(r+1)
                        uneg.remove(row-col)
                        upos.remove(row+col)


                    ucols.remove(col)
        solve(0)
        return ans

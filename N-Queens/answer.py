class Solution:
    def solveNQueens(self, n: int) -> list[list[str]]:
        
        board= ["."*n for i in range (n)]
        ans=[]
        urows,ucols,upos,uneg=set(),set(),set(),set() # u = used / blocked
        # uneg and upos are negeative and postive diagonal - where positive is the diagonal with positive slope
        def solve(r): # r= row number 
            row=r
            if row not in urows:
                urows.add(row)
                for col in range (0,n):
                    if col not in ucols:
                        ucols.add(col)
                        if row-col  not in uneg and row+col not in upos:
                            uneg.add(row-col)
                            upos.add(row+col)

                            board[row]=board[row][:col]+'Q'+board[row][col+1:]
                            
                            if len(ucols)==n: # and len(urows)==n and all other sets of lenght n  
                                ans.append(board.copy())
                            
                            solve(r+1)
                            board[row]=board[row][:col]+'.'+board[row][col+1:]
                            uneg.remove(row-col)
                            upos.remove(row+col)


                        ucols.remove(col)
                urows.remove(row)
        solve(0)
        return ans
        

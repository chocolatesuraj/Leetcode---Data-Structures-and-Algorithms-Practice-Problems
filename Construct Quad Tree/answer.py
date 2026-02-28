"""
# Definition for a QuadTree node.
class Node:
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight
"""

class Solution:
    def construct(self, grid: List[List[int]]) -> 'Node':
        rows=len(grid)
        cols=len(grid[0])


        def tree(grid,row1,col1,row2,col2):
            # print("-"*10)
            # print(row1,col1,row2,col2)
            if(row1==row2 and col1==col2):
                return Node(grid[row1][col1],True,None,None,None,None)

            topleft =tree(grid,row1,col1,(row2+row1-1)//2,(col2+col1-1)//2)
            bottomleft =tree(grid,(row2+row1+1)//2,col1,row2,(col2+col1-1)//2)
            bottomright =tree(grid,(row2+row1+1)//2,(col2+col1+1)//2,row2,(col2))
            topright =tree(grid,row1,(col2+col1+1)//2,(row2+row1-1)//2,col2)

            if(topleft.isLeaf==True and bottomleft.isLeaf==True and bottomright.isLeaf==True and topright.isLeaf==True and  topleft.val == bottomleft.val and bottomleft.val==bottomright.val and bottomright.val==topright.val ):
                return Node(bottomleft.val,True,None,None,None,None)
            else:
                return Node(bottomleft.val,False,topleft,topright,bottomleft,bottomright)

        return tree(grid,0,0,rows-1,cols-1)

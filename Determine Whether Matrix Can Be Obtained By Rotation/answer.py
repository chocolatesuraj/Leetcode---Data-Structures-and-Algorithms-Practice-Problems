class Solution:
    def findRotation(self, mat: List[List[int]], target: List[List[int]]) -> bool:
        m=len(mat)
        # 0,1 -> 1,3
        def rotate():
            for i in range(m):
                for j in range(m):
                    if(i<j):
                        mat[i][j],mat[j][i]=mat[j][i],mat[i][j]
            for i in range(m):
                for j  in range(int(m//2)):
                    mat[i][j],mat[i][m-1-j]=mat[i][m-1-j],mat[i][j]
        for i  in range(4):
            if mat == target:
                return True
            rotate()
        return False

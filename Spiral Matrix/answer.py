class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        rs,re=0,len(matrix[0])-1
        cs,ce=0,len(matrix)-1
        ans=[]
        while(rs<=re and cs<=ce):
            # print(rs,re,cs,ce)
            for i in range(rs,re+1):
                ans.append(matrix[cs][i])
            for i in range(cs+1,ce+1):
                ans.append(matrix[i][re])
            if(cs!=ce):
                for i in range(re-1,rs-1,-1):
                    ans.append(matrix[ce][i])
            if(rs!=re):
                for i in range(ce-1,cs,-1):
                    ans.append(matrix[i][rs])
                
            rs+=1
            re-=1
            cs+=1
            ce-=1
        return ans


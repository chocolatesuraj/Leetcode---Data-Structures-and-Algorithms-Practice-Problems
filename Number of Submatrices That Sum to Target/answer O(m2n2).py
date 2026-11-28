class Solution:
    def numSubmatrixSumTarget(self, matrix: list[list[int]], target: int) -> int:
        '''
        x x x x x
        x x x o o
        x x x o o
        '''
        
        store=[[0]*len(matrix[0]) for i in range(len(matrix))]
        # print(store)
        for i in range (len(matrix)):
            for j in range(len(matrix[0])):
                if i == 0:
                    if j == 0:
                        store[i][j]=matrix[i][j]
                    else:
                        store[i][j]=store[i][j-1]+matrix[i][j]
                elif i != 0:
                    if j != 0:
                        store[i][j]= store[i-1][j] +store[i][j-1]+ matrix[i][j] - store[i-1][j-1]
                    elif j==0:
                        # print("     ",i,j)
                        store[i][j]= store[i-1][j] + matrix[i][j]
        # print(store)

        ans=0
        for x1 in range (len(matrix)):
            for y1 in range(len(matrix[0])):
                for x2 in range (x1,len(matrix)):
                    for y2 in range(y1,len(matrix[0])):
                        # if x2>=x1 and y2>=y1:
                            total=store[x2][y2]
                            if x1>0:
                                total=total-store[x1-1][y2]
                            if y1>0:
                                total= total - store[x2][y1-1]
                                if x1>0 and y1>0:
                                    total = total + store[x1-1][y1-1]
                            if total == target:
                                ans+=1
        return ans



                    

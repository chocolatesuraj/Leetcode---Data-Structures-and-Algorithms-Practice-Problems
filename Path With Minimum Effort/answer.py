class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        m=len(heights)
        n=len(heights[0])
        vis=[[0]*n for i in range(m)]
        heap=[] # heap of nodes
        heapq.heappush(heap,[0,0,0]) # effort, i,j
        ans=float("inf")
        while(heap):
            effort,i,j=heapq.heappop(heap)
            # print(effort,i,j)
            if(vis[i][j]==1):
                continue
            else:
                vis[i][j]=1
            if(i==m-1 and j==n-1):
                return effort

            if(i+1<m):
                heapq.heappush(heap,[max(effort,abs(heights[i][j]-heights[i+1][j])),i+1,j])
            if(i-1>=0):
                heapq.heappush(heap,[max(effort,abs(heights[i][j]-heights[i-1][j])),i-1,j])
            if(j+1<n):
                heapq.heappush(heap,[max(effort,abs(heights[i][j]-heights[i][j+1])),i,j+1])
            if(j-1>=0):
                heapq.heappush(heap,[max(effort,abs(heights[i][j]-heights[i][j-1])),i,j-1])

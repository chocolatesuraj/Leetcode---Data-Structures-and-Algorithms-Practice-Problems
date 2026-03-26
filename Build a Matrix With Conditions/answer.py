class Solution:
    def buildMatrix(self, k: int, rowConditions: List[List[int]], colConditions: List[List[int]]) -> List[List[int]]:
        
        def topo(conds):

            adj=defaultdict(list)
            visited=[0]*(k+1)
            for prev,nex in conds:
                adj[prev].append(nex)
            ans=[]
            loop=False
            def dfs(node):
                if visited[node]==0:
                    visited[node]=2 # 2 = temporary visit state
                    for nex in adj[node]:
                        if visited[nex]==0:
                            dfs(nex)
                        if visited[nex]==2:
                            nonlocal loop
                            loop=True
                    visited[node]=1
                    ans.append(node)

                    

            for i in range(1,k+1):
                if loop==True:
                    return False

                if visited[i]==0:
                    dfs(i)
            if loop==True:
                return False
            ret={}
            taken=set()
            for i,ele in enumerate(ans):
                ret[ele]=k-i-1
                taken.add(k-i-1)
            return ret,taken

        td = topo(rowConditions)
        rl = topo(colConditions)
        
        
    
        if td==False or rl==False:
            return []

        rmap,takenrows=td
        cmap,takencols=rl

        rows= set([i for i in range(0,k)]) - takenrows
        cols= set([i for i in range(0,k)]) - takencols
        ans=[[0]*k for i in range(k)]

        for i in range(1,k+1):
            if i in rmap:
                r=rmap[i]
            else:
                r=rows.pop()
            if i in cmap:
                c=cmap[i]
            else:
                c=cols.pop()
            # print(i,r,c)
            ans[r][c]=i
        return ans

        


            


               

        

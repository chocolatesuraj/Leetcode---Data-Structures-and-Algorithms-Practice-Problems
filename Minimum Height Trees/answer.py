class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        adj=defaultdict(set)
        if n==1:
            return [0]
        if n==2:
            return [0,1]
        degree=defaultdict(int)
        for a,b in edges:
            adj[a].add(b)
            adj[b].add(a)
            degree[a]+=1
            degree[b]+=1 

        removed=set()
        leafs=[node for node in adj.keys() if degree[node]==1 ]
        newleafs=[]
        while len(adj)>2 or leafs:
            if leafs==[]:
                leafs=newleafs
                newleafs=[]
                
            leaf=leafs.pop()

            for nei in adj[leaf]:
                degree[nei]-=1
                if degree[nei]==1:
                    newleafs.append(nei)
            del adj[leaf]

        ans= [node for node in adj.keys()]
        return ans


        

    

        
         

        
        



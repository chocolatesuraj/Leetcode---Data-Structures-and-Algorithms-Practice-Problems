class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj=defaultdict(list)
        for d,s in prerequisites:
            adj[s].append(d)
        
        visited=[0]*numCourses
        temp=set()
        # ans=
        def dfs(node):
            # print(node,temp)
            for dst in adj[node]:
                # print("dst",dst)
                if(visited[node]==0):
                    
                    if(node in temp):
                        return False
                    temp.add(node)
                    if dfs(dst)==False:
                        return False
                    temp.remove(node)
            visited[node]=1
            return True
        for pos,i in enumerate(visited):
            if(i==0):
                if dfs(pos)==False:
                    return False
        return True


                


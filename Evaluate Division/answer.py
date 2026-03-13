class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        adj=defaultdict(list)
        allowed=set()
        for i,eqn in enumerate(equations):
            a,b=eqn
            adj[a].append([b,values[i]])
            adj[b].append([a,1/values[i]])
            allowed.add(a)
            allowed.add(b)

        def dfs(neu,den): 
            if neu in visited:
                return False
            visited.add(neu)
            
            for d,val in adj[neu]:
                if d==den:
                    return val
                r= dfs(d,den)
                if r!=False:
                    return val * r
            return False 

        ans=[]
        for q in queries:
            n,d=q
            if (n not in allowed or d not in allowed):
                ans.append(-1.0)
            else:
                visited=set()
                r=dfs(n,d)
                if r==False:
                    ans.append(-1.0)
                else:
                    ans.append(r)
        return ans
            


class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        hashmap=defaultdict(list)
        for prereq,course in prerequisites:
            hashmap[prereq].append(course)
        print(hashmap)
        order=set()
        def dfs(val,check):
            for node in hashmap[val]:
                ans=False
                if(vis[node]==0):
                    vis[node]=1
                    if(node==check):
                        return True
                    ans=ans or dfs(node,check)
                    if ans:
                        return ans 
            return False


        ans=[]
        for pre,course in queries :
            vis=[0]*numCourses
            ret=dfs(pre,course)
            ans.append(ret)
        return ans 
           


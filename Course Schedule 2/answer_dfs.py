class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        hashmap=defaultdict(set)
        for course,prereq in prerequisites:
            hashmap[prereq].add(course)

        visited=[0]*numCourses
        ans=[]
        loop=False
        tempvis=set()

        def dfs(val):
            nonlocal loop
            while hashmap[val]:
                
                node = hashmap[val].pop()
                if(node in tempvis):
                        loop=True
                        return 
                if visited[node]==0:
                    
                    visited[node]=1
                    tempvis.add(node)
                    dfs(node)
                    tempvis.remove(node)
                    ans.append(node)

        i=0
        while i<numCourses:
            if(visited[i]==1):
                i+=1
                continue
            visited[i]=1
            tempvis.add(i)
            dfs(i)
            tempvis.remove(i)
            ans.append(i)
        ans.reverse()
        # print("loop",loop)
        if loop == True:
            return []
        return ans
        

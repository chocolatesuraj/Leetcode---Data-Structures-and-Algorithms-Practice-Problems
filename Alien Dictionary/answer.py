class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        adj=defaultdict(set)
        for word in words:
            for ch in word:
                adj[ch]=set()
        flag=False
        def compare(i,j):
            nonlocal flag
            prev=words[j-1]
            curr=words[j]
            if i>=len(prev):
                return
            if i>=len(curr):
                flag=True
                return

            if prev[i] == curr[i]:
                compare(i+1,j)
            else: # letters in ith pos not equal 
                adj[prev[i]].add(curr[i])
        for j in range(1,len(words)):
            compare(0,j)
        if flag:
            return ""
        ans=[]
        visited=[0]*26
        loop=False
        def dfs(node):
            nonlocal loop
            pos=ord(node)-ord("a")
            if visited[pos]==1:
                return
            if visited[pos]==2:
                loop=True 
                return 
            visited[pos]=2
            for nex in adj[node]:
                dfs(nex)
            visited[pos]=1
            ans.append(node)
        for i in range(0,26):
            c=chr(ord("a")+i)
            if visited[i]==0 and c in adj:
                dfs(chr(ord("a")+i))
        if loop==True:
            return ""

        ret=""
        for c in ans[::-1]:
            ret+=c
        return ret
        





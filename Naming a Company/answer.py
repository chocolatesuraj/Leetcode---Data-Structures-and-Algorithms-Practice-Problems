class Solution:
    def distinctNames(self, ideas: list[str]) -> int:
        suffix=defaultdict(set)
        for word in ideas:
            a,b=word[0],word[1:]
            suffix[a].add(b)
        keys=list(suffix.keys())
        ans=0
        for i in range(0,len(keys)):
            for j in range(i+1,len(keys)):
                intseclen=len(suffix[keys[i]].intersection(suffix[keys[j]]))
                ans+=(len(suffix[keys[i]])-intseclen)*(len(suffix[keys[j]])-intseclen)

        return ans*2


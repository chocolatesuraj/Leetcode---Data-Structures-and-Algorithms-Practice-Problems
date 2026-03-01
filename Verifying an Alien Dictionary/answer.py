class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        hashmap={}
        for i,c in enumerate(order):
            hashmap[c]=i
        
        def compare(word1,word2):
            i=0
            while(i<min(len(word1),len(word2))):
            
                if(hashmap[word1[i]] < hashmap[word2[i]]):
                    return True 
                elif(hashmap[word1[i]] == hashmap[word2[i]]):
                    i+=1
                else:
                    return False 
            if(len(word1)<=len(word2)):
                return True
            return False

        for i in range(1,len(words)):
            if compare(words[i-1],words[i])==False:
                return False
        return True




            


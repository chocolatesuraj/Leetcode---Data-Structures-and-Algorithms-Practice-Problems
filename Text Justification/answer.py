class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        temp=[]
        l=0 # length of all words with space to check if less than maxWidth
        wl=0 # len of all words without space
        ans=[] # final ans to return 
        i=0 # track processed word 
        extra=0 
        s=0 
        while  i <len(words):
            word=words[i]
            # print(word,temp)
            if len(temp)==0:
                temp.append(word)
                l+=len(word)
                wl+=len(word)
                i+=1
            elif l+1+len(word)<=maxWidth:
                temp.append(word)
                l=l+1+len(word)
                wl+=len(word)
                i+=1
            else:
                if len(temp)==1:
                    tans=temp[0]
                    tans+=" "*(maxWidth-len(tans))
                    ans.append(tans)
                    # ans.append(tans)
                    # i+=1
                    temp=[]
                    l=0
                    wl=0
                else:
                    spaces=maxWidth-wl
                    s=spaces//(len(temp)-1)
                    extra=spaces%(len(temp)-1)
                    tans=temp[0]
                    for w in temp[1:]:
                        tans+=" "*s
                        if extra:
                            tans+=" "
                            extra-=1
                        tans+=w
                    
                    ans.append(tans)

                temp=[]
                l=0
                wl=0
        tans=temp[0]
        for w in temp[1:]:
            tans+=" "
            tans+=w
        tans+=" "*(maxWidth-len(tans))
        ans.append(tans)

        return ans

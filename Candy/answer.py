class Solution:
    #10 20 9 8 7 6 5
    def candy(self, ratings: List[int]) -> int:
        candy=[1]*len(ratings)

        for i,rating in enumerate(ratings):
            if i-1>=0 and rating>ratings[i-1]:
                candy[i]=candy[i-1]+1

        for i in range(len(ratings)-1,-1,-1):
            if i+1<len(ratings) and ratings[i]>ratings[i+1]:
                candy[i]=max(candy[i],candy[i+1]+1)

        return sum(candy)

                    
            
            


            

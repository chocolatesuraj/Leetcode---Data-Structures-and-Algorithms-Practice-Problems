class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        maxele=-1
        for i in range(len(arr)-1,-1,-1):
            prevmax=maxele
            maxele=max(maxele,arr[i])
            arr[i]=prevmax
        return arr

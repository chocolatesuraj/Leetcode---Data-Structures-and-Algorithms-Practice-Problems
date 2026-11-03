class Solution:
    def findMedianSortedArrays(self, nums1: list[int], nums2: list[int]) -> float:
      total=len(nums1)+len(nums2)
      half = int(total/2)
      if len(nums2)<len(nums1):
        nums1,nums2=nums2,nums1

      

      f,b=0,len(nums1)

      while(f<=b):
        # print("fb",f,b)
        m=int((f+b)/2)
        m2=half-m
        # print(m,m2)
        # print(L1,R1,L2,R2)
        if m2-1>=len(nums2):
            f=m+1
            continue
        if m2-1<-1:
            b=m-1
            continue
        L1 = nums1[m-1] if m-1>=0 else -float("inf")
        L2 = nums2[m2-1] if m2-1>=0 else -float("inf")
        R1 = nums1[m] if m<len(nums1) else float("inf")
        R2 = nums2[m2] if m2<len(nums2) else float("inf")

        # print(L1,R1,L2,R2)

        if L1<=R2 and L2<=R1:
            if total%2==0:
                return (min(R2,R1)+max(L1,L2))/2
            else:
                return min(R2,R1)
        elif L1>R2:
            b=m-1
        else:
            f=m+1

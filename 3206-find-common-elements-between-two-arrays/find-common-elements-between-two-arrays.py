class Solution:
    def findIntersectionValues(self, nums1: List[int], nums2: List[int]) -> List[int]:
        a1,a2=0,0
        n1=set(nums1)
        n2=set(nums2)
        for i in nums1:
            if i in n2:
                a1+=1
        for i in nums2:
            if i in n1:
                a2+=1
        return [a1,a2]
        

        
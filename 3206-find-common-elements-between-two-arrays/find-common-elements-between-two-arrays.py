class Solution:
    def findIntersectionValues(self, nums1: List[int], nums2: List[int]) -> List[int]:
        a1,a2=0,0
        n1=set(nums1)
        n2=set(nums2)
        for i in n1:
            if i in n2:
                a1+=nums1.count(i)
        for i in n2:
            if i in n1:
                a2+=nums2.count(i)
        return [a1,a2]
        

        
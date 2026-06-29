class Solution:
    def findIntersectionValues(self, nums1: List[int], nums2: List[int]) -> List[int]:
        a1,a2=0,0
        for i in set(nums1):
            if i in nums2:
                a1+=nums1.count(i)
        for i in set(nums2):
            if i in nums1:
                a2+=nums2.count(i)
        return [a1,a2]
        

        
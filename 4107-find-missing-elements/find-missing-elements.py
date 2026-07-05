class Solution:
    def findMissingElements(self, nums: List[int]) -> List[int]:
        if len(nums)==max(nums)+1-min(nums):
            return []
        l=list(range(min(nums),max(nums)+1))
        for i in nums:
            l.remove(i)
        return l

        
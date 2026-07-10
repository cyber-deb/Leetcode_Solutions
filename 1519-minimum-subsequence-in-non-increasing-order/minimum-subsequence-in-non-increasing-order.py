class Solution:
    def minSubsequence(self, nums: List[int]) -> List[int]:
        l=[]
        nums.sort()
        while sum(l)<=sum(nums):
            l.append(nums.pop())
        return l
        
class Solution:
    def repeatedNTimes(self, nums: List[int]) -> int:
        for i in set(nums):
            if nums.count(i)==len(nums)//2:
                return i
        
class Solution:
    def absDifference(self, nums: List[int], k: int) -> int:
        nums.sort()
        return abs(sum(nums[-1:-(k+1):-1])-sum(nums[:k]))
        
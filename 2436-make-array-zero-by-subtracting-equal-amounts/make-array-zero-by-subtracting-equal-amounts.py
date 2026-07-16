class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        s=set(nums)-{0}
        return len(s)
class Solution:
    def concatWithReverse(self, nums: list[int]) -> list[int]:
        k=list(reversed(nums))
        return nums+k

        
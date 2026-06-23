class Solution:
    def sumOfUnique(self, nums: List[int]) -> int:
        r=0
        for i in nums:
            if nums.count(i)==1:
                r+=i
        return r        
class Solution:
    def minMoves(self, nums: List[int]) -> int:
        k=max(nums)
        c=0
        for i in nums:
            while i!=k:
                i+=1
                c+=1
        return c

        
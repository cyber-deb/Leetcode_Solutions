class Solution:
    def missingMultiple(self, nums: List[int], k: int) -> int:
        l=list(range(k,(k*(len(nums)+1))+1,k))
        for i in l:
            if i not in nums:
                return i
class Solution:
    def smallestEqual(self, nums: List[int]) -> int:
        l=[]
        for i in range(len(nums)):
            if i%10==nums[i]:
                l.append(i)
        return min(l) if l else -1
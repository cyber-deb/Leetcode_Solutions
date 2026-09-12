class Solution:
    def smallestAbsent(self, nums: List[int]) -> int:
        k=(sum(nums)//len(nums))+1
        k= 1 if k<=0 else k
        while True:
            if k in nums:
                k+=1
            else:
                return k
        
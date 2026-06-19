class Solution:
    def pivotInteger(self, n: int) -> int:
        nums=list(range(1,n+1))

        lsum=0
        rsum=sum(nums)
        for i in range(len(nums)):
            rsum-=nums[i]
            if lsum==rsum:
                return nums[i]
            lsum+=nums[i]
        return -1
        
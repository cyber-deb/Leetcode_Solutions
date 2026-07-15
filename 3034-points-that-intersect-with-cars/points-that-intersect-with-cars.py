class Solution:
    def numberOfPoints(self, nums: List[List[int]]) -> int:
        s=set()
        for i in nums:
            s.update(range(i[0],i[1]+1))
        return len(s)
        
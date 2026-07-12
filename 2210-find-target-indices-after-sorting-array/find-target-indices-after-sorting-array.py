class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        l=[]
        for i,x in enumerate(sorted(nums)):
            if target==x:
                l.append(i)
        return l 
from itertools import combinations
class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        res,x=0,0
        for r in range(1, len(nums)+1):
            for c in combinations(nums, r):
                for i in c:
                    x^=i
                res+=x
                x=0
        return res

     
        
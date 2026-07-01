class Solution:
    def getSneakyNumbers(self, nums: List[int]) -> List[int]:
        l=[]
        for i in set(nums):
            if i not in l and nums.count(i)>1:
                l.append(i)
        return l
        
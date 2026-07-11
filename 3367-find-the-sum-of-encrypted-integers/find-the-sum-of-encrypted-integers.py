class Solution:
    def sumOfEncryptedInt(self, nums: List[int]) -> int:
        s=0
        for i in range(len(nums)):
            s+=int(str(max(list(map(int,str(nums[i])))))*len(str(nums[i])))
        return s
        
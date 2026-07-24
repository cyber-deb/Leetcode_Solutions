class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        for i in range(2**len(nums[0])):
            if bin(i)[2:].zfill(len(nums[0])) not in nums:
                return bin(i)[2:].zfill(len(nums[0]))
        
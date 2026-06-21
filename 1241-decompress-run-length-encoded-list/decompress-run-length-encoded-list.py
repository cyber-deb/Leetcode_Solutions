class Solution:
    def decompressRLElist(self, nums: List[int]) -> List[int]:
        k=[]
        for i in range(1,len(nums),2):
            k+=[nums[i]]*nums[i-1]
        return k

        
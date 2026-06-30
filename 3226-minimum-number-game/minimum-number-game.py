class Solution:
    def numberGame(self, nums: List[int]) -> List[int]:
        arr=[]
        for i in range(len(nums)//2):
            arr+=[min(nums)]
            nums.remove(min(nums))
            arr.insert(len(arr)-1,min(nums))
            nums.remove(min(nums))
        return arr
        
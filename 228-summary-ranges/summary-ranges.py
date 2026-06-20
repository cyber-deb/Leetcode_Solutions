class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        if len(nums) == 0:
            return []
        k = []
        s = [str(nums[0])]
        c = 0
        for i in range(len(nums)-1):
            if nums[i+1]==nums[i]+1:
                c+=1
            else:
                if c!=0:
                    k.append(s[0]+"->"+str(nums[i]))
                else:
                    k.append(str(nums[i]))
                s=[str(nums[i + 1])]
                c=0
        if c!=0:
            k.append(s[0]+"->"+str(nums[-1]))
        else:
            k.append(str(nums[-1]))
        return k
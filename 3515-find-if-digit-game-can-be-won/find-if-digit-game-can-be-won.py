class Solution:
    def canAliceWin(self, nums: List[int]) -> bool:
        dums=[]
        aums=[]
        for i in nums:
            if len(str(i)) == 1:
                dums.append(i)
            else:
                aums.append(i)
        return sum(dums)!=sum(aums)
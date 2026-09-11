class Solution:
    def validateCoupons(self,code:List[str],businessLine:List[str],isActive:List[bool]) -> List[str]:
        order={'electronics':0,'grocery':1,'pharmacy':2,'restaurant':3}
        ans=[]
        for i in range(len(code)):
            if code[i] and all(c.isalnum() or c=='_' for c in code[i]) and businessLine[i] in order and isActive[i]:
                ans.append((order[businessLine[i]],code[i]))
        ans.sort()
        return [x[1] for x in ans]
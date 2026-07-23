class Solution:
    def garbageCollection(self,garbage:List[str],travel:List[int])->int:
        for i in range(1,len(travel)):
            travel[i]+=travel[i-1]
        ans=0
        for s in garbage:
            ans+=len(s)
        for c in "GPM":
            for i in range(len(garbage)-1,-1,-1):
                if c in garbage[i]:
                    if i>0:
                        ans+=travel[i-1]
                    break
        return ans
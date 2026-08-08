class Solution:
    def findRestaurant(self,list1:List[str],list2:List[str])->List[str]:
        d={v:i for i,v in enumerate(list1)}
        ans=[]
        mn=float('inf')
        for i,s in enumerate(list2):
            if s in d:
                t=i+d[s]
                if t<mn:
                    mn=t
                    ans=[s]
                elif t==mn:
                    ans.append(s)
        return ans
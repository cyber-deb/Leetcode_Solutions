class Solution:
    def countLargestGroup(self, n: int) -> int:
        if n<10:
            return n
        d={1:1,2:1,3:1,4:1,5:1,6:1,7:1,8:1,9:1}
        for i in range(10,n+1):
            s=sum(list(map(int,str(i))))
            if s not in d:
                d[s]=1
            else:
                d[s]+=1
        return list(d.values()).count(max(d.values()))

        
        
class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        l=[]
        c=0
        for i in range (left,right+1):
            if len(str(i))==1:
                l.append(i)
            elif '0' not in set(str(i)):
                for j in list(str(i)):
                    if i%int(j)!=0:
                        break
                    c+=1
                if c==len(str(i)):
                    l.append(i)
                c=0
        return l
                

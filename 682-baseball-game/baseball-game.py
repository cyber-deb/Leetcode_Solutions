class Solution:
    def calPoints(self, operations: List[str]) -> int:
        k=[]
        def check(x):
            if x>(2**31)-1:
                return (2**31)-1
            elif x<-(2**31):
                return -(2**31)
            else:
                return x
        for i in operations:
            if i not in ["C","D","+"]:
                k.append(check(int(i)))
            elif i=='C':
                k.pop()
            elif i=='D':
                k.append(check(2*k[-1]))
            else:
                k.append(check(k[-1]+k[-2]))
        return sum(k)
            


        
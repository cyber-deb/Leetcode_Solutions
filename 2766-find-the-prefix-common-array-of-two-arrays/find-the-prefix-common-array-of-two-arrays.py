class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        c=0
        s1=set()
        s2=set()
        ans=[]
        for i in range(len(A)):
            if A[i]==B[i]:
                c+=1
            else:
                if A[i] in s2:
                    c+=1
                if B[i] in s1:
                    c+=1
            s1.add(A[i])
            s2.add(B[i])
            ans.append(c)
        return ans
        
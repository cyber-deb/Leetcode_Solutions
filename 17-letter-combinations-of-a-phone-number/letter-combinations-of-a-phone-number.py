from itertools import product as pt
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if digits=='':
            return []
        ans=[]
        d={'2':"abc",'3':"def",'4':"ghi",'5':"jkl",'6':"mno",'7':"pqrs",'8':"tuv",'9':"wxyz"}
        for pair in pt(*(d[x] for x in digits)):
            ans.append(''.join(pair))
        return ans

        
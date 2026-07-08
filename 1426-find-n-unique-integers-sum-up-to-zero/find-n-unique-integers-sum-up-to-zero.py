class Solution:
    def sumZero(self, n: int) -> List[int]:
        ans=[]
        if n%2!=0:
            ans=[0]
        for i in range(n//2):
            ans+=[-(i+1),(i+1)]
        return ans
        
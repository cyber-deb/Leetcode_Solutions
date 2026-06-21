class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        ans=[]
        for num in range(left,right+1):
            t=num
            valid=True
            while t>0:
                digit=t%10
                if digit==0 or num%digit!=0:
                    valid=False
                    break
                t//=10
            if valid:
                ans.append(num)
        return ans
                

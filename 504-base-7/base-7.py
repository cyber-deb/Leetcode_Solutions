class Solution:
    def convertToBase7(self, num: int) -> str:
        if num==0:
            return '0'
        a=num<0
        k=''
        num=abs(num)
        while num:
            k+=str(num%7)
            num//=7
        if a:
            k+='-'
        return k[::-1]

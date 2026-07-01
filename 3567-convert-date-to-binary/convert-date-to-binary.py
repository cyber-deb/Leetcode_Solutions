class Solution:
    def convertDateToBinary(self, date: str) -> str:
        l=date.split('-')
        k=''
        for i in l:
            k=k+bin(int(i))[2:]+'-'
        return k[:-1]
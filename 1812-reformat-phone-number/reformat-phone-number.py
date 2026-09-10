class Solution:
    def reformatNumber(self, number: str) -> str:
        number=number.replace('-','')
        number=number.replace(" ","")
        ans=''
        while number:
            if len(number)>4:
                ans+=number[:3]+'-'
                number=number[3:]
            elif len(number)>3:
                ans+=number[:2]+'-'
                number=number[2:]
            else:
                ans+=number
                number=''
        return ans
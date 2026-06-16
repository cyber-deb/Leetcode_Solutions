class Solution:
    def processStr(self, s: str) -> str:
        r=''
        for i in s:
            if i=='*':
                r=r[:len(r)-1:]
            elif i=='#':
                r*=2
            elif i=='%':
                r=r[::-1]
            elif i.islower():
                r+=i
        return r
        
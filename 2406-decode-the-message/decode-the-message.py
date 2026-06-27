class Solution:
    def decodeMessage(self, key: str, message: str) -> str:
        key=key.replace(' ','')
        check=[]
        d={}
        k=0
        for i in key:
            if i not in check:
                d[i]=chr(97+k)
                k+=1
                check.append(i)
        d[' ']=' '
        s=''
        for i in message:
            s+=d[i]
        return s
        
        
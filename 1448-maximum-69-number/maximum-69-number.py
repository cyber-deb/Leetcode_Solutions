class Solution:
    def maximum69Number (self, num: int) -> int:
        x=str(num)
        if set(x)=={'9'}:
            return num

        for i in range (len(x)):
            if x[i]=='6':
                x=x[0:i]+'9'+x[i+1:]
                break
        return int(x)

        
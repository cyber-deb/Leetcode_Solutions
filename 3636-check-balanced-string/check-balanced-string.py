class Solution:
    def isBalanced(self, num: str) -> bool:
        even=[]
        odd=[]
        for i in range(0,len(num)-1,2):
            even.append(int(num[i]))
            odd.append(int(num[i+1]))
        if len(num)%2==1:
            even.append(int(num[-1]))
        return sum(even)==sum(odd)

        
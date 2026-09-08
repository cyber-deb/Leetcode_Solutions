class Solution:
    def numDifferentIntegers(self, word: str) -> int:
        nums=[]
        x=''
        for c in word:
            if c.isdigit():
                x+=c
            elif x:
                nums.append(int(x))
                x=''
        if x:
            nums.append(int(x))
        return len(set(nums))
        
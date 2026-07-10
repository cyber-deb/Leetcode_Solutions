class Solution:
    def minTimeToType(self, word: str) -> int:
        s=0
        a=ord('a')
        ptr=a
        for i in word:
            k=abs(ord(i)-ptr)
            s+=(1+min(k,26-k))
            ptr=ord(i)
        return s
class Solution:
    def digitSum(self, s: str, k: int) -> str:
        n=''
        while len(s)>k:
            l=[s[i:i+k] for i in range(0,len(s),k)]
            for i in l:
                n+=str(sum(list(map(int,i))))
            s=n
            n=''
        return s
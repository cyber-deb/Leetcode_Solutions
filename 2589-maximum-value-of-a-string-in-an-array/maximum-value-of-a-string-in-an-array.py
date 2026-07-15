class Solution:
    def maximumValue(self, strs: List[str]) -> int:
        m=0
        for i in strs:
            if i.isdigit():
                m=max(int(i),m)
            else:
                m=max(m,len(i))
        return m
        
class Solution:
    def buddyStrings(self, s: str, goal: str) -> bool:
        if len(s)!=len(goal):
            return False
        d=[i for i in range(len(s)) if s[i]!=goal[i]]
        if len(d)==2:
            return s[d[0]]==goal[d[1]] and s[d[1]]==goal[d[0]]
        if len(d)==0:
            return len(set(s))<len(s)
        return False
        
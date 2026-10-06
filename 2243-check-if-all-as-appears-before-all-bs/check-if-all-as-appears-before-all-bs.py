class Solution:
    def checkString(self, s: str) -> bool:
        if len(set(s))==1:
            return True
        return False if 'a' in s[s.index('b'):] else True
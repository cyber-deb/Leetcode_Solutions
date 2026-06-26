class Solution:
    def longestPalindrome(self, s: str) -> str:
        if len(s)==1:
            return s
        for i in range(len(s),0,-1):
            for j in range(len(s)-i+1):
                part=s[j:j+i]
                if part==part[::-1]:
                    return part
        return ''
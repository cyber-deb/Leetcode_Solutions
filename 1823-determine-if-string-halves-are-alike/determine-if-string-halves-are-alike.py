class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        s=s.lower()
        vowel=['a','e','i','o','u']
        c1,c2=0,0
        for i in s[:len(s)//2]:
            if i in vowel:
                c1+=1
        for i in s[len(s)//2:]:
            if i in vowel:
                c2+=1
        return c1==c2
        
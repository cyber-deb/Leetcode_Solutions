class Solution:
    def possibleStringCount(self, word: str) -> int:
        ans=1
        count=1
        for i in range(1,len(word)):
            if word[i]==word[i - 1]:
                count+=1
            else:
                ans+=count-1
                count=1
        ans+=count-1
        return ans
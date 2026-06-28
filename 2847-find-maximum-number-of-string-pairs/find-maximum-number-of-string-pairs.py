class Solution:
    def maximumNumberOfStringPairs(self, words: List[str]) -> int:
        check=set()
        c=0
        for i in words:
            if i[::-1] in words and i not in check and i!=i[::-1]:
                c+=1
                check.add(i[::-1])
        return c

        
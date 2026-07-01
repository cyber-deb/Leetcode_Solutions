class Solution:
    def kthCharacter(self, k: int) -> str:
        word='a'
        r=''
        while len(word)<k:
            for i in word:
                r+=chr(ord(i)+1)
            word+=r
            r=''
        return word[k-1]



        
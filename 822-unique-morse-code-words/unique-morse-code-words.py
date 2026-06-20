class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        m=[".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        k=[]
        r=''
        for i in words:
            for j in range(len(i)):
                r+=m[ord(i[j])-97]
            k.append(r)
            r=''
        return len(set(k))

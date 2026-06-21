class Solution:
    def numberOfLines(self, widths: List[int], s: str) -> List[int]:
        r=0
        c=0
        for i in s:
            r+=widths[ord(i)-97]
            if r>100:
                c+=1
                r=widths[ord(i)-97]
        return [c+1,r]

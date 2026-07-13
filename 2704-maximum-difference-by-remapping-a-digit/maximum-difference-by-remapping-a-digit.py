class Solution:
    def minMaxDifference(self, num: int) -> int:
        l=str(num)
        m=str(num)
        i=0
        while i<len(l):
            if l[i]!='9':
                l=l.replace(l[i],'9')
                break
            i+=1
        m=m.replace(m[0],'0')
        return int(l)-int(m)
        
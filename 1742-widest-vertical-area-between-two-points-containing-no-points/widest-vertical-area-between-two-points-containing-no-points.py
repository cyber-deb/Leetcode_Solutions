class Solution:
    def maxWidthOfVerticalArea(self, points: List[List[int]]) -> int:
        l=[]
        for i in points:
            l.append(i[0])
        x=[]
        l.sort()
        for i in range(len(l)-1):
            x.append(abs(l[i]-l[i+1])) 
        return max(x)
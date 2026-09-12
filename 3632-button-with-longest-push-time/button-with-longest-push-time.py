class Solution:
    def buttonWithLongestTime(self, events: List[List[int]]) -> int:
        mx=events[0][1]
        ans=events[0][0]
        prev=events[0][1]
        for i,t in events[1:]:
            d=t-prev
            if d>mx or (d==mx and i<ans):
                mx=d
                ans=i
            prev=t
        return ans
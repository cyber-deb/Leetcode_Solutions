class Solution:
    def countDaysTogether(self, arriveAlice: str, leaveAlice: str, arriveBob: str, leaveBob: str) -> int:
        month=[31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        def convert(s):
            m,d=map(int,s.split('-'))
            day=sum(month[:m-1])+d
            return day
        a1,a2=convert(arriveAlice),convert(arriveBob)
        l1,l2=convert(leaveAlice),convert(leaveBob)
        start=max(a1,a2)
        stop=min(l1,l2)
        return max(0,stop-start+1)


class Solution:
    def calPoints(self, operations: List[str]) -> int:
        ans=[]
        for a in operations:
            if a.isdigit() or "-" in a:
                ans.append(int(a))
            elif a=='+':
                ans.append(ans[-1]+ans[-2])
            elif a=="D":
                ans.append(ans[-1]*2)
            else:
                ans.pop()
        return sum(ans)

        
class Solution:
    def elevatorRequests(self, n: int, requests: list[int]) -> int:
        s=requests[0]
        for i in range(len(requests)-1):
            s+=abs(requests[i+1]-requests[i])
        return s
class Solution:
    def partition(self, s: str) -> List[List[str]]:
        ans=[]
        path=[]
        def dfs(start):
            if start==len(s):
                ans.append(path[:])
                return
            for end in range(start,len(s)):
                t=s[start:end+1]
                if t==t[::-1]:
                    path.append(t)
                    dfs(end+1)
                    path.pop()
        dfs(0)
        return ans
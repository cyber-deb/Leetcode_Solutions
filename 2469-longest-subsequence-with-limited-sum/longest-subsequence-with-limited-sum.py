class Solution:
    def answerQueries(self, nums: List[int], queries: List[int]) -> List[int]:
        nums.sort()
        ans = []
        for q in queries:
            s = 0
            c = 0
            for x in nums:
                if s + x <= q:
                    s += x
                    c += 1
                else:
                    break
            ans.append(c)

        return ans
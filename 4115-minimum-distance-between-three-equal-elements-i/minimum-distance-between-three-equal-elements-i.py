class Solution:
    def minimumDistance(self, nums: List[int]) -> int:
        pos = {}
        for i, x in enumerate(nums):
            pos.setdefault(x, []).append(i)
        ans = float("inf")
        for indices in pos.values():
            if len(indices) >= 3:
                for i in range(len(indices) - 2):
                    ans = min(ans, 2 * (indices[i + 2] - indices[i]))
        return -1 if ans == float("inf") else ans
    
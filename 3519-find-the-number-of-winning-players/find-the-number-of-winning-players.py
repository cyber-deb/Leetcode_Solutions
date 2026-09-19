class Solution:
    def winningPlayerCount(self, n: int, pick: List[List[int]]) -> int:
        count = [[0] * 11 for _ in range(n)]
        for player, color in pick:
            count[player][color] += 1
        ans = 0
        for player in range(n):
            for color in range(11):
                if count[player][color] > player:
                    ans += 1
                    break
        return ans
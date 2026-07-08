class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        starts=[row[0] for row in paths]
        for row in paths:
            if row[1] not in starts:
                return row[1]

        
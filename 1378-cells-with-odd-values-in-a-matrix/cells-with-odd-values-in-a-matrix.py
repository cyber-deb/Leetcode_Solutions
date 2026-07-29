class Solution(object):
    def oddCells(self, m, n, indices):
        mat = [[0] * n for _ in range(m)]
        ind = sum(indices, [])
        for x in range(len(ind)):
            if x % 2 == 0:
                mat[ind[x]] = [v + 1 for v in mat[ind[x]]]
            else:
                for i in range(m):
                    mat[i][ind[x]] += 1
        count = 0
        for row in mat:
            for x in row:
                if x % 2 != 0:
                    count += 1
        return count
        
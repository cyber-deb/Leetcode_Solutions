class Solution:
    def areSimilar(self, mat: List[List[int]], k: int) -> bool:
        n=len(mat[0])
        k%=n
        for i in range(len(mat)):
            if i%2==0:
                if mat[i][k:]+mat[i][:k]!=mat[i]:
                    return False
            else:
                if mat[i][-k:]+mat[i][:-k]!=mat[i]:
                    return False
        return True
        
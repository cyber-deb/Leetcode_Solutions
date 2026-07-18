class Solution:
    def minCosts(self, cost: List[int]) -> List[int]:
        ans=[]
        mn=float('inf')
        for c in cost:
            mn=min(mn,c)
            ans.append(mn)
        return ans
                
        
        
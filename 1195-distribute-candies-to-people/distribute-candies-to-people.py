class Solution:
    def distributeCandies(self, candies: int, num_people: int) -> list[int]:
        ans=[0]*num_people
        i=0
        while candies!=0:
            if candies>=i+1:
                candies-=(i+1)
                ans[i%num_people]+=i+1
                i+=1
            else:
                ans[i%num_people]+=candies
                candies=0
        return ans
        
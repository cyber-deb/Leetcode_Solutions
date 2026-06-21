# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:
        high=n
        low=1
        while low<=high:
            mid=(high+low)//2
            k=guess(mid)
            if k==0:
                return mid
            elif k==(-1):
                high=mid-1
            elif k==1:
                low=mid+1
            
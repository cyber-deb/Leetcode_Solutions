class Solution:
    def countTestedDevices(self, batteryPercentages: List[int]) -> int:
        ans = 0
        for bat in batteryPercentages:
            if bat>0:
                if bat-ans>=0:
                    bat-=ans
                else:
                    bat=0
            if bat>0:
                ans+=1
        return ans
        
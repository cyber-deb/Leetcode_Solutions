class Solution:
    def reformatDate(self, date: str) -> str:
        d=date.split()
        s=d[2]+'-'
        mon={'Jan':'01','Feb':'02','Mar':'03','Apr':'04','May':'05','Jun':'06','Jul':'07','Aug':'08','Sep':'09','Oct':'10','Nov':'11','Dec':'12'}
        s+=mon[d[1]]+'-'
        s=s+'0'+d[0][0] if len(d[0])==3 else s+d[0][0:2]
        return s


